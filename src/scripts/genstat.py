"""
Functions to process source files to generate statistics about the book.
"""
from pathlib import Path
from pdb import set_trace
from collections import OrderedDict


def remove_tex_command(line):
    """
    Find latex command in a line and remove it.
    """
    latex_cmds = ["\cos", "\sin", "\circ", "\otimes", "\circledcirc",
                  "\index", "\\flushleft", "\\tcolorbox",
                  "\cdot", "\chhc",
                  "\\frac", "\quad", "\qquad", "\\rightarrow",
                  "\lbrace", "\\rbrace", "\lettrine", "\color",
                  "\lbrack", "\\rbrack", "\\text",
                  "\emph", "\\footnote", "\\begin", "\end",
                  "\centering", "\includegraphics", "\caption",
                  "\label", "\\ref", "\mathbb", "\section", "\subsection",
                  "\\textrm", "\item", "\phantom", "\\vspace", "mybio",
                  "\pm", "\ldots", "\\bf", "\it", "\longrightarrow",
                  "\overset", "\subsubsection", "\[", "\]", "\,",
                  "mydef", "\\ne", "\le", "\delta", "\\alpha", "\\beta",
                  "\mu", "\\nu", "\epsilon", "\hline", "\\bar", "\\tilde",
                  "\\approx", "\propto", "\\vec", "\op", "\pageref"]
    line_ = line
    for cmd in latex_cmds:
        line_ = line_.replace(cmd, " ")
    no_tex = False
    while not no_tex:
        try:
            i_start = line_.find("\\")
            i_end = line_.find("{")
            if (i_start > -1) and (i_end > i_start):
                line_ = line_.replace(line_[i_start:(i_end+1)], ' ')
            else:
                no_tex = True
        except:
            no_tex = True
    return line_

def remove_inline_equation(line):
    line_ = line
    no_eqs = False
    cnt = 0
    while not no_eqs:
        if '$' in line_:
            i_start = line_.find('$')
            i_next = line_[i_start+1:].find('$')
            if (i_start > -1) and (i_next > -1):
                i1 = i_start
                i2 = i_start + i_next + 2
                line_ = line_.replace(line_[i1:i2], ' ')
            else:
                line_ = line_.replace('$', ' ')
            cnt += 1
            if cnt > 100:
                ne_eqs = True
                set_trace()
        else:
            no_eqs = True

    return line_

def remove_numbers(line):
    line_ = line
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for s in numbers:
        line_ = line_.replace(s, ' ')
    return line_

def replace_symbols(symbols, line):
    line_ = line
    for s in symbols:
        line_ = line_.replace(s, ' ')
    return line_

def remove_extra_symbols(line):
    line_ = line
    es = ['\\', '=', '^', "_", '{']
    for s in es:
        line_ = line_.replace(s, ' ')
    return line_

def remove_simple_words(line):
    # sws = [" is ", " it ", " an ", " at ", " of ", " if ",
    #        " of "]
    sws = ["is", "it", "an", "at", "of", "if",
           "of"]
    line_ = line
    for sw in sws:
        line_ = line_.replace(sw, ' ')
    return line_

def clean_line(line):
    sep_symb = ['.', ',', '}', ';', ':', '--',
                '`', "'", '!', '?','\n',
                '(', ')', '*', '+', '&', '%',
                '[', ']']
    # line_ = remove_simple_words(line)
    line_ = replace_symbols(sep_symb, line)
    line_ = remove_tex_command(line_)
    line_ = remove_inline_equation(line_)
    line_ = remove_numbers(line_)
    line_ = remove_extra_symbols(line_)
    return line_

def process_tex_file(fpath):
    with open(fpath) as f:
        data = f.readlines()
        clean_data = ""
        # remove end of line
        for i, line in enumerate(data):
            cline = clean_line(line).replace('\n', ' ')
            if len(cline) > 1 and (not "/pics/" in cline):
                clean_data += cline
    return clean_data

def count_words(fpath):
    res = process_tex_file(fpath)
    words = [w.lower() for w in set(res.split()) if len(w.strip()) > 1]
    set_of_words = sorted(words)
    counted_words = OrderedDict()
    for w in set_of_words:
        counted_words[w] = res.lower().count(w)

    return counted_words


if "__main__" == __name__:
    paths = [("ack", Path("../00Preface/acknowledgement.tex")),
             ("preface", Path("../00Preface/preface.tex")),
             ("intro", Path("../01Introduction/introduction.tex")),
             ("numbers", Path("../02NumbersFunctions/numbers_functions.tex")),
             ("vectors", Path("../03ArrowsVectors/arrows_vectors.tex")),
             ("operators", Path("../04Operators/operators.tex")),
             ("tensors", Path("../05Tensors/tensors.tex")),
             ("fun", Path("../06FunProfit/fun_profit.tex")),
             ("answers", Path("../07Answers/answers.tex"))]
    res = OrderedDict()
    for name, path in paths:
        try:
            res[name] = count_words(path)
        except Exception as e:
            print("Failed to process {} : {}".format(name, e))

    for name, resdict in res.items():
        with open(name+".txt", "w") as f:
            for k, v in resdict.items():
                f.write("{}\t{}\n".format(k, v))
    #set_trace()
