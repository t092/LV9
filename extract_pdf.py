import sys
import subprocess

try:
    import pypdf
except ImportError:
    print("Installing pypdf...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypdf', '--user'])
    import pypdf

try:
    reader = pypdf.PdfReader('L02.pdf')
    with open('l02_text.txt', 'w', encoding='utf-8') as f:
        for page in reader.pages:
            f.write(page.extract_text() + '\n')
    print('SUCCESS')
except Exception as e:
    print(f'ERROR: {e}')
