# -*- mode: python -*-

block_cipher = None


a = Analysis(['../src/urh/main.py'],
             pathex=['/Users/boss/urh/data'],
             binaries=[( '/usr/local/lib/librtlsdr.dylib', 'librtlsdr.dylib' ),
                       ( '/usr/local/lib/libhackrf.dylib', 'libhackrf.dylib' ),
                       ( '/usr/local/lib/libmpc.dylib', 'libmpc.dylib' ),
                       ( '/usr/local/lib/libmpfr.dylib', 'libmpfr.dylib'),
                       ( '/usr/local/lib/libgmp.dylib', 'libgmp.dylib'),
                       ( '/usr/local/lib/libisl.dylib', 'libisl.dylib'),
                       ( '/usr/local/lib/libfftw3.dylib', 'libfftw3.dylib')
                       ( '/usr/local/lib/libusb-1.0.0.dylib', 'libusb.dylib')
                       ( '/usr/local/lib/libuhd.dylib', 'libuhd.dylib' ),
                       ( '/usr/local/lib/libportaudio.dylib', 'libportaudio.dylib'),
                       ( '/usr/local/lib/libairspy.dylib', 'libairspy.dylib'),
                       ( '/usr/local/lib/libLimeSuite.dylib', 'libLimeSuite.dylib')],
             datas=[('../src/urh/plugins/*.py', 'urh/plugins'),
                    ('../src/urh/plugins/InsertSine/*', 'urh/plugins/InsertSine'),
                    ('../src/urh/plugins/MessageBreak/*', 'urh/plugins/MessageBreak'),
                    ('../src/urh/plugins/NetworkSDRInterface/*', 'urh/plugins/NetworkSDRInterface'),
                    ('../src/urh/plugins/RfCat/*', 'urh/plugins/RfCat'),
                    ('../src/urh/plugins/ZeroHide/*', 'urh/plugins/ZeroHide')],
             hiddenimports=['six','packaging', 'packaging.version', 'packaging.specifiers', 'html', 'html.parser', 'pyaudio'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='data/icons/appicon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='urh')
app = BUNDLE(coll,
             name='Universal Radio Hacker.app',
             icon='data/icons/appicon.icns',
             bundle_identifier='jopohl.UniversalRadioHacker')