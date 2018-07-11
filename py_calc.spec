# -*- mode: python -*-

block_cipher = None


a = Analysis(['py_calc.py'],
             pathex=['C:\\Users\\Qbit\\pycharmprojects\\python_calculator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='py_calc',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
