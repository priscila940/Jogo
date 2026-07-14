[Setup]
AppName=GlitchOut
AppVersion=1.0
DefaultDirName={autopf}\GlitchOut
DefaultGroupName=GlitchOut
UninstallDisplayIcon={app}\GlitchOut.exe
Compression=lzma2
SolidCompression=yes
OutputDir=Output_Installer
OutputBaseFilename=GlitchOut_Setup

[Files]
; Aqui dizemos para o Inno Setup pegar o .exe que o PyInstaller acabou de gerar
Source: "dist\GlitchOut.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\GlitchOut"; Filename: "{app}\GlitchOut.exe"
Name: "{commondesktop}\GlitchOut"; Filename: "{app}\GlitchOut.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar um atalho na Área de Trabalho"; GroupDescription: "Atalhos adicionais:"
