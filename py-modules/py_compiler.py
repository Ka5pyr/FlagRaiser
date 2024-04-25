import PyInstaller.__main__

def compile(py_full_path):
    PyInstaller.__main__.run([
        py_full_path,
        '--onefile',
        '--collect-submodules=ipaddress',
        '--collect-submodules=psutil',
        '--collect-submodules=rich',
        '--collect-submodules=json',
        '--collect-submodules=textwrap',
        '--hidden-import=./py-modules/check_processor',
        '--hidden-import=./py-modules/format_message',
        '--hidden-import=./py-modules/net_info'
    ])