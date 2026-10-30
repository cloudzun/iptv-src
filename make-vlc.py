import re, sys, pathlib
d = pathlib.Path(__file__).parent
srcname = sys.argv[1] if len(sys.argv) > 1 else "tv.m3u"
src = (d / srcname).read_text(encoding="utf-8").splitlines()
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
print(f"generated tv-vlc.m3u from {srcname}: {n} channels")
