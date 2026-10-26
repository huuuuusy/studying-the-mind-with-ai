"""Build the printable handout (handout.pdf) from the guides in this repository.

    python3 docs/handout/make_handout.py        # needs XeLaTeX (TeX Live), rsvg-convert and Pillow
    python3 docs/handout/make_handout.py zh     # the Chinese handout, handout.zh.pdf, from the .zh.md pages

For listeners who cannot reach GitHub: the essentials on paper. The text is taken from
docs/start-here.md, the four part guides, docs/glossary.md and resources/working-together.md, so
the handout changes when they do; rerun this script after editing them. Animated figures and
relationship diagrams are left out; links inside the repository become plain text, links outside
it become footnotes.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
REPO_URL = "https://github.com/huuuuusy/studying-the-mind-with-ai"
NAVY, INK2, MUTE, RULE = "1E2A5E", "465069", "8A91A3", "DDE1EA"
CHECK = {1: "1F4FA3", 2: "0E8C7E", 3: "9A6700"}


LANG = {
    "en": dict(
        suffix=".md", out="handout.pdf",
        start={"The one question", "The talk in four parts", "Why now", "How the talk ended"},
        part={"What the talk showed", "The question behind it", "What it gives back to psychology", "Key readings", "How they connect"},
        means=r"What it means\.", index="Index", item="- **{t}.** {d}",
        glossary="# Glossary\n\nOne line per term; the full entries, with sources, are in docs/glossary.md.\n\n",
        fonts="",
        pdftitle="Studying the Human Mind with AI: handout and reading companion",
        subtitle=r"From Behavioral Analysis to Role Simulation\\[2pt]{\large Handout and reading companion for the talk}",
        online="Online:", scan="scan for the repository", footer="Studying the Human Mind with AI · handout",
        intro="Everything you need to start is in this handout, also if GitHub is slow or unreachable where you are.",
        readmore=r"""\section*{Read more}
In the repository: \texttt{resources/reading-path.md} (a step-by-step reading path), \texttt{resources/examples/} (one card per key reading), \texttt{resources/students.md} (reading list by area of psychology), \texttt{resources/README.md} (by part of the talk) and \texttt{resources/literature.md} (about 300 references, field-wide).

{\small\color{mute}Text and diagrams: CC BY-NC 4.0. The talk's drawings: \copyright{} 2026 Shiyu Hu, all rights reserved. Built from the repository by \texttt{docs/handout/make\_handout.py}.}"""),
    "zh": dict(
        suffix=".zh.md", out="handout.zh.pdf",
        start={"一个问题", "讲座的四个部分", "为什么是现在", "讲座怎样结束"},
        part={"讲座里讲了什么", "背后的问题", "反过来，对心理学有什么用", "重点必读", "它们之间的关系"},
        means="含义。", index="索引", item="- **{t}：**{d}",
        glossary="# 词典\n\n每个术语一行；完整的词条和出处见 docs/glossary.zh.md。\n\n",
        fonts=r"""\usepackage{xeCJK}
\setCJKmainfont{Hiragino Sans GB W3}[BoldFont={Hiragino Sans GB W6}]
\setCJKmonofont{Hiragino Sans GB W3}
""",
        pdftitle="Studying the Human Mind with AI：讲座讲义与配套阅读指南",
        subtitle=r"From Behavioral Analysis to Role Simulation\\[2pt]{\large 从行为分析到角色模拟 · 讲座讲义与配套阅读指南}",
        online="在线版：", scan="扫码访问仓库", footer="Studying the Human Mind with AI · 讲义",
        intro="开始所需的一切都在这份讲义里；访问 GitHub 很慢或无法访问时也能用。",
        readmore=r"""\section*{继续阅读}
在仓库里：\texttt{resources/reading-path.zh.md}（一步一步的阅读路线），\texttt{resources/examples/}（每篇重点必读一张卡片），\texttt{resources/students.md}（按心理学方向的阅读清单，英文），\texttt{resources/README.md}（按讲座部分，英文），以及 \texttt{resources/literature.md}（约 300 篇参考文献，全领域，英文）。

{\small\color{mute}文字与图表：CC BY-NC 4.0。讲座插图：\copyright{} 2026 Shiyu Hu，保留所有权利。由仓库中的 \texttt{docs/handout/make\_handout.py zh} 生成。}"""),
}


def esc(t):
    t = t.replace("\\", "\\textbackslash{}")
    for a, b in [("&", "\\&"), ("%", "\\%"), ("#", "\\#"), ("_", "\\_"), ("$", "\\$"), ("{", "\\{"), ("}", "\\}"),
                 ("~", "\\textasciitilde{}"), ("^", "\\textasciicircum{}")]:
        t = t.replace(a, b)
    return t


def inline(t):
    """Markdown inline -> LaTeX. Code spans first, so their contents are not touched again."""
    keep = []

    def stash(s):
        keep.append(s)
        return f"\x00{len(keep) - 1}\x00"

    def link(m):
        text, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://")):
            return stash(inline(text) + r"\footnote{\url{" + url.replace("%", "\\%").replace("#", "\\#") + "}}")
        return stash(inline(text))

    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, t)  # links first: their text may hold code spans
    t = re.sub(r"`([^`]+)`", lambda m: stash(r"\texttt{" + esc(m.group(1)) + "}"), t)
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
    t = re.sub(r"(?<![A-Za-z0-9_*])\*(?!\s)(.+?)(?<!\s)\*(?![A-Za-z0-9_*])", r"\\emph{\1}", t)
    t = t.replace("κ", r"$\kappa$").replace("→", r"$\rightarrow$").replace("≥", r"$\geq$").replace("…", r"\ldots{}")
    t = t.replace("☐", r"$\square$").replace("—", "---").replace("–", "--")
    return re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], t)


def figure(src, workdir, width):
    if src.endswith(".gif"):
        return ""
    path = os.path.normpath(os.path.join(ROOT, "docs", src))
    out = os.path.join(workdir, os.path.basename(src).replace(".svg", ".pdf"))
    if src.endswith(".png"):   # slide images from the talk, as JPEG to keep the PDF small
        from PIL import Image
        out = out[:-4] + ".jpg"
        Image.open(path).convert("RGB").save(out, quality=78, optimize=True)
    else:
        subprocess.run(["rsvg-convert", "-f", "pdf", "-o", out, path], check=True)
    return rf"\begin{{center}}\includegraphics[width={width}\linewidth]{{{os.path.basename(out)}}}\end{{center}}"


def table(lines):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines if not re.match(r"^\|[\s\-|:]+\|$", l.strip())]
    n = len(rows[0])
    widths = {3: [0.26, 0.56, 0.18], 4: [0.19, 0.39, 0.19, 0.23]}.get(n, [1 / n] * n)
    if n == 3 and not rows[0][0]:
        widths = [0.06, 0.42, 0.52]
    if n == 3 and rows[0][0] in ("Area", "方面"):   # what each side brings, in the guide to working together
        widths = [0.16, 0.42, 0.42]
    spec = "|".join(r">{\raggedright\arraybackslash}p{%.3f\linewidth}" % (w - 0.02) for w in widths)
    body = [r"\rowcolor{rule}" + " & ".join(r"\textbf{" + inline(c) + "}" for c in rows[0]) + r" \\ \hline"]
    body += [" & ".join(inline(c) for c in r) + r" \\ \hline" for r in rows[1:]]
    size = r"\footnotesize" if n >= 4 else r"\small"
    return "{" + size + r"\renewcommand{\arraystretch}{1.2}\begin{tabular}{|" + spec + "|}\\hline\n" + "\n".join(body) + "\n\\end{tabular}}"


def convert(md, workdir, drop_first_heading=False, shift=0):
    out, i, lines = [], 0, md.splitlines()
    para = []

    def flush():
        if para:
            out.append(inline(" ".join(para)))
            para.clear()

    while i < len(lines):
        l = lines[i]
        s = l.strip()
        if s.startswith("```mermaid"):
            flush()
            j = i + 1
            while not lines[j].strip().startswith("```"):
                j += 1
            i = j + 1
            continue
        if s.startswith("```"):
            flush()
            j = i + 1
            code = []
            while not lines[j].strip().startswith("```"):
                code.append(lines[j].strip())
                j += 1
            out.append(r"\begin{lstlisting}" + "\n" + "\n".join(code) + "\n" + r"\end{lstlisting}")
            i = j + 1
            continue
        if s.startswith("<p>") or s.startswith("</p>"):
            i += 1
            continue
        m = re.match(r'<img src="([^"]+)"(?: width="(\d+)%")?', s)
        if m:
            flush()
            w = 0.40 if "plate" in m.group(1) else 0.85 if "slides/" in m.group(1) else 0.46
            out.append(figure(m.group(1), workdir, f"{w:.2f}"))
            i += 1
            continue
        m = re.match(r"^!\[[^\]]*\]\(([^)]+)\)", s)
        if m:
            flush()
            out.append(figure(m.group(1), workdir, "0.9"))
            i += 1
            continue
        m = re.match(r"^(#+) (.+)$", s)
        if m:
            flush()
            level = len(m.group(1)) + shift
            if drop_first_heading and level == 1 + shift:
                drop_first_heading = False
            else:
                cmd = {1: "section", 2: "section", 3: "subsection"}.get(level, "subsubsection")
                out.append(rf"\{cmd}*{{{inline(m.group(2))}}}")
            i += 1
            continue
        if s.startswith("|"):
            flush()
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                j += 1
            out.append(table(lines[i:j]))
            i = j
            continue
        if re.match(r"^- ", s):
            flush()
            items = []
            while i < len(lines) and (re.match(r"^\s*- ", lines[i]) or (lines[i].startswith("  ") and lines[i].strip())):
                li = lines[i]
                if li.strip().startswith("```"):
                    j = i + 1
                    code = []
                    while not lines[j].strip().startswith("```"):
                        code.append(lines[j].strip())
                        j += 1
                    items[-1] += "\n" + r"\begin{lstlisting}" + "\n" + "\n".join(code) + "\n" + r"\end{lstlisting}"
                    i = j + 1
                    continue
                if re.match(r"^\s*- ", li):
                    items.append(inline(li.strip()[2:]))
                else:
                    items[-1] += " " + inline(li.strip())
                i += 1
            out.append(r"\begin{itemize}[leftmargin=*,itemsep=2pt]" + "\n" + "\n".join(r"\item " + it for it in items) + "\n" + r"\end{itemize}")
            continue
        if re.match(r"^\d+\. ", s):   # numbered list; continuation lines are indented
            flush()
            items = []
            while i < len(lines) and (re.match(r"^\d+\. ", lines[i].strip()) or (lines[i].startswith("   ") and lines[i].strip())):
                li = lines[i].strip()
                if re.match(r"^\d+\. ", li):
                    items.append(re.sub(r"^\d+\. ", "", li))
                else:
                    items[-1] += " " + li        # joined before conversion, so bold may span lines
                i += 1
            out.append(r"\begin{enumerate}[leftmargin=*,itemsep=2pt]" + "\n" + "\n".join(r"\item " + inline(it) for it in items) + "\n" + r"\end{enumerate}")
            continue
        if not s:
            flush()
        else:
            para.append(s)
        i += 1
    flush()
    return "\n\n".join(x for x in out if x)


def main(lang="en"):
    if not shutil.which("rsvg-convert") or not shutil.which("xelatex"):
        sys.exit("needs rsvg-convert and xelatex")
    L = LANG[lang]
    work = tempfile.mkdtemp()

    def read(*p):
        """A page in the chosen language, without its language-switch line."""
        p = list(p[:-1]) + [p[-1][:-3] + L["suffix"]]
        text = open(os.path.join(ROOT, *p), encoding="utf-8").read()
        return re.sub(r"\A(\*\*English\*\*|\[English\]).*\n+", "", text)

    def sections(md, keep):
        """Keep the '## ' sections whose titles are in keep, in their original order, with the page title."""
        parts = re.split(r"(?m)^(## .+)$", md)
        out = [parts[0]]
        for head, body in zip(parts[1::2], parts[2::2]):
            if head[3:].strip() in keep:
                out.append(head + body)
        text = "".join(out)
        return re.sub(r"(?m)^---\n.*\Z", "", text, flags=re.S)

    start = sections(read("docs", "start-here.md"), L["start"])
    parts = [sections(read("docs", f), L["part"])
             for f in ("part1-people-next-to-machine.md", "part2-people-as-the-answer.md",
                       "part3-people-we-make.md", "part4-ai-in-your-research.md")]
    gloss_md = read("docs", "glossary.md")
    gloss = []
    for block in re.split(r"(?m)^## ", gloss_md)[1:]:
        title, _, body = block.partition("\n")
        if title.strip() == L["index"]:
            continue
        items = re.findall(r"(?m)^### (.+)\n\n\*\*" + L["means"] + r"\*\* (.+)$", body)
        if items:
            gloss.append(f"### {title.strip()}\n\n" + "\n".join(L["item"].format(t=t, d=d) for t, d in items))
    glossary = L["glossary"] + "\n\n".join(gloss)
    projects = read("resources", "working-together.md")
    subprocess.run(["rsvg-convert", "-f", "pdf", "-o", os.path.join(work, "qr.pdf"),
                    os.path.join(ROOT, "assets", "qr-studying-the-mind-with-ai-black.svg")], check=True)
    doc = r"""\documentclass[10.5pt,a4paper]{article}
\usepackage[a4paper,margin=1.9cm,footskip=0.9cm]{geometry}
\usepackage{fontspec}
\setmainfont{SourceSans3}[Extension=.otf,UprightFont=*-Regular,BoldFont=*-Bold,ItalicFont=*-RegularIt,BoldItalicFont=*-BoldIt]
\setmonofont{texgyrecursor}[Extension=.otf,UprightFont=*-regular,BoldFont=*-bold,Scale=0.95]
""" + L["fonts"] + r"""\usepackage[table]{xcolor}
\definecolor{navy}{HTML}{""" + NAVY + r"""}\definecolor{ink2}{HTML}{""" + INK2 + r"""}\definecolor{mute}{HTML}{""" + MUTE + r"""}\definecolor{rule}{HTML}{""" + RULE + r"""}
\usepackage{graphicx,tabularx,enumitem,listings,titlesec,fancyhdr,amssymb}
\usepackage[hidelinks]{hyperref}
\hypersetup{pdfauthor={Shiyu Hu},pdftitle={""" + L["pdftitle"] + r"""}}
\lstset{basicstyle=\ttfamily\small,backgroundcolor=\color{rule!45},frame=none,breaklines=true,columns=fullflexible,aboveskip=4pt,belowskip=4pt,xleftmargin=4pt,xrightmargin=4pt}
\titleformat*{\section}{\Large\bfseries\color{navy}}
\titleformat*{\subsection}{\large\bfseries\color{navy}}
\titlespacing*{\section}{0pt}{1.0em}{0.4em}\titlespacing*{\subsection}{0pt}{0.8em}{0.3em}
\raggedright\setlength{\parindent}{0pt}\setlength{\parskip}{0.45em}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\footnotesize\color{mute}""" + L["footer"] + r"""}\fancyfoot[R]{\footnotesize\color{mute}\thepage}
\begin{document}
\begin{minipage}[t]{0.70\linewidth}\vspace{0pt}
{\fontsize{22}{26}\selectfont\bfseries\color{navy} Studying the Human Mind with AI}\\[4pt]
{\Large\color{ink2} """ + L["subtitle"] + r"""}\\[8pt]
{\color{ink2}Shiyu Hu\\ """ + L["online"] + r"""\\ \url{""" + REPO_URL + r"""}}\\[6pt]
{\small\color{mute}""" + L["intro"] + r"""}
\end{minipage}\hfill
\begin{minipage}[t]{0.24\linewidth}\vspace{0pt}\centering\includegraphics[width=\linewidth]{qr.pdf}\\[-2pt]{\scriptsize\color{mute}""" + L["scan"] + r"""}\end{minipage}

\vspace{6pt}{\color{rule}\rule{\linewidth}{1pt}}
""" + convert(start, work, drop_first_heading=True) + r"""

""" + "\n\n".join(r"\clearpage" + "\n" + convert(p, work) for p in parts) + r"""

\clearpage
""" + convert(glossary, work) + r"""

\clearpage
""" + convert(projects, work) + r"""

""" + L["readmore"] + r"""
\end{document}
"""
    tex = os.path.join(work, "handout.tex")
    open(tex, "w", encoding="utf-8").write(doc)
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "handout.tex"], cwd=work,
                           capture_output=True, text=True)
        if r.returncode:
            print(r.stdout[-3000:])
            sys.exit("xelatex failed; the .tex is in " + work)
    shutil.copy(os.path.join(work, "handout.pdf"), os.path.join(HERE, L["out"]))
    print("wrote", os.path.join(HERE, L["out"]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "en")
