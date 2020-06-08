import re
separator='(:\s*\n|։\s*\n|\.\s*\n|․\s*\n)'

def breaches_from_borders(style_change_borders,last_index):
    style_breaches = []
    current = 0
    for border in style_change_borders:
        style_breaches.append( (current,border-1) )
        current = border
    style_breaches.append( (style_change_borders[-1],last_index) )
    return style_breaches

def get_paragraphs_of(text):
    # using ()just to save the real punctation mark, every even paragraph will contain only accured punctation-mark
    paragraphs = re.split(separator, text)
    for i in range(0, len(paragraphs) - 1, 2):  # adding missing splitt-punctation mark to the end of paragraph
        paragraphs[i] += paragraphs[i + 1]
    del paragraphs[1::2]  # deleting single even paragraphs with accured punctation-mark
    return paragraphs

def get_starts_of_paragraphs(paragraphs):
    start_of_paragraph = {}
    i = 1
    length = 0
    for item in paragraphs:
        start_of_paragraph[i] = length
        i += 1
        length += (len(item))
    return start_of_paragraph


def starts_pars_for_annot(text):
    text = re.sub(r"\\r\\r", '\r\r', text)
    fixed_text = ""
    fixed_spans = []
    results = re.finditer(r"#Text=", text)
    prev = next(results)
    starts = []
    ends = []
    for m in results:
        fixed_start = prev.start(0) - len("#Text=") * len(fixed_spans)
        fixed_end = m.start(0) - 1 - len("#Text=") * (len(fixed_spans) + 1)
        fixed_span = (fixed_start, fixed_end)
        fixed_spans.append(fixed_span)
        fixed_text += text[prev.start(0) + len("#Text="): m.start(0)]
        starts.append(fixed_start)
        ends.append(fixed_end)
        prev = m
    fixed_start = prev.start(0) - len("#Text=") * len(fixed_spans)
    starts.append(fixed_start)
    ends.append(fixed_end)
    fixed_end = len(text) - 1 - len("#Text=") * (len(fixed_spans) + 1)
    fixed_span = (fixed_start, fixed_end)
    fixed_spans.append(fixed_span)
    fixed_text += text[prev.start(0) + len("#Text="):]
    pars = []
    for i in range(len(starts)-1):
        pars.append(fixed_text[starts[i]:starts[i+1]])
    return starts,pars

def annot_get_starts_of_paragraphs(text):
    return starts_pars_for_annot(text)[0]

def annot_get_paragraphs_of(text):
    return starts_pars_for_annot(text)[1]
