from pathlib import Path
import json, re, zipfile

root=Path(__file__).resolve().parents[1]
skill=root/'skills/humanizer-fr'
manifest=json.loads((root/'plugin.json').read_text(encoding='utf-8'))
overlay=json.loads((root/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
version=manifest['version']
assert re.fullmatch(r'\d+\.\d+\.\d+',version), 'Expected semantic plugin version'
assert overlay['version']==version, 'Plugin versions differ'
assert manifest['name']==overlay['name']=='humanizer-fr'
assert manifest['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
assert manifest['extensions']['com.openai']['interface']==overlay['interface']
assert (root/'SKILL.md').read_bytes()==(skill/'SKILL.md').read_bytes(), 'Root skill mirror differs'
assert (root/'references/exemples-fr.md').read_bytes()==(skill/'references/exemples-fr.md').read_bytes(), 'Example mirror differs'
text=(skill/'SKILL.md').read_text(encoding='utf-8')
skill_version=re.search(r'^  version: "([^"]+)"',text,re.M).group(1)
assert len(re.findall(r'^### FR\d+\.',text,re.M))==18
generic=text.split('## Generic English patterns from upstream Humanizer',1)[1].split('## What not to change',1)[0]
assert len(re.findall(r'^\d+\.',generic,re.M))==26
dist=root/'dist'; dist.mkdir(exist_ok=True)
def archive(path,entries):
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,strict_timestamps=False) as z:
        for source,target in entries: z.write(source,target)
    with zipfile.ZipFile(path) as z: assert z.testzip() is None
plugin_entries=[(root/p,p) for p in ('plugin.json','.codex-plugin/plugin.json')]
plugin_entries.extend((p,p.relative_to(root).as_posix()) for p in sorted(skill.rglob('*')) if p.is_file())
archive(dist/f'humanizer-fr-plugin-{version}.zip',plugin_entries)
archive(dist/f'humanizer-fr-skill-{skill_version}.zip',[(p,p.relative_to(skill).as_posix()) for p in sorted(skill.rglob('*')) if p.is_file() and 'agents' not in p.relative_to(skill).parts])
print(f'Validated plugin {version}, skill {skill_version}; archives written to {dist}')
