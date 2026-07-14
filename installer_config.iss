; installer_config.iss
; Script de configuração do Inno Setup para criar o Instalador .exe

[Setup]
AppName=Glitch Out
AppVersion=1.0
DefaultDirName={autopf}\GlitchOut
DefaultGroupName=Glitch Out
UninstallDisplayIcon={app}\GlitchOut.exe
Compression=lzma2
SolidCompression=yes
OutputDir=Output_Installer
OutputBaseFilename=GlitchOut_Setup

[Files]
; Aqui apontamos para o .exe que o PyInstaller gerou
Source: "dist\GlitchOut.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Cria o atalho no Menu Iniciar
Name: "{group}\Glitch Out"; Filename: "{app}\GlitchOut.exe"
; Cria o atalho na Área de Trabalho do jogador (sua solicitação!)
Name: "{autodesktop}\Glitch Out"; Filename: "{app}\GlitchOut.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar um atalho na Área de Trabalho"; GroupDescription: "Atalhos adicionais:"; Flags: unchecked

[Run]
; Opção para rodar o jogo assim que a instalação terminar
Filename: "{app}\GlitchOut.exe"; Description: "Lançar Glitch Out"; Flags: nowait postinstall skipifsilent
