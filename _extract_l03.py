import sys
try:
    import pypdf
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypdf', '--user'])
    import pypdf

reader = pypdf.PdfReader('L03.pdf')
with open('l03_text.txt', 'w', encoding='utf-8') as f:
    for page in reader.pages:
        txt = page.extract_text()
        if txt: f.write(txt + '\n')
print('SUCCESS')
