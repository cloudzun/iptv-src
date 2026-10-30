import re, sys, pathlib
d = pathlib.Path(__file__).parent
src = (d / "tv.m3u").read_text(encoding="utf-8").splitlines()
out = ["#EXTM3U"]
UA = "AptvPlayer-UA"
i, n = 0, 0
while i < len(src):
    line = src[i]
    if line.startswith("#EXTINF"):
        grp = re.search(r'group-title="([^"]*)"', line)
        name = line.split(",")[-1]
        out.append(f'#EXTINF:-1 group-title="{grp.group(1)}",{name}' if grp else f"#EXTINF:-1,{name}")
        out.append(f"#EXTVLCOPT:http-user-agent={UA}")
        if i + 1 < len(src) and src[i+1].strip().startswith("http"):
            out.append(src[i+1].strip()); i += 2; n += 1; continue
    i += 1
(d / "tv-vlc.m3u").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"regenerated tv-vlc.m3u with {n} channels")
