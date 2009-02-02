# TODO
# - check the license?
# - package dedicated server: ioUrTded
# - what of is ioUrbanTerror.* and where should it be installed?
Summary:	FPS best be described as a Hollywood tactical shooter
Name:		urbanterror
Version:	4.1
Release:	0.3
Group:		Applications/Games
Source0:	http://dls.urt.voxel.net/q3ut4/UrbanTerror_41_FULL.zip
# NoSource0-md5:	1370306ea236f65f595e7ca70765e469
# too huge for df (700mb)?
NoSource:	0
License:	?
URL:		http://www.urbanterror.net/
Requires:	hicolor-icon-theme
Source1:	%{name}.sh
Source2:	%{name}.autodlrc
Source3:	%{name}.desktop
Source4:	%{name}.png
Requires:	quake3
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gamedir	%{_prefix}/share/games/quake3

%description
Urban Terror could best be described as a Hollywood tactical shooter;
it is realism based to a certain extent (environments/weapons/player
models), but also goes by the motto "fun over realism" (fast gameplay
and lots of action). This combination of reality and action results in
a very unique, enjoyable and addictive game.

Urban Terror uses the GPL licensed ioquake3 engine, however the Urban
Terror datafiles are not freely redistributable.

%prep
%setup -q -n UrbanTerror

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{gamedir}/q3ut4}
%ifarch %{ix86}
install ioUrbanTerror.i386 $RPM_BUILD_ROOT%{_bindir}/ioUrbanTerror
install ioUrTded.i386 $RPM_BUILD_ROOT%{_bindir}/ioUrTded
%endif
%ifarch %{x8664}
install ioUrbanTerror.x86_64 $RPM_BUILD_ROOT%{_bindir}/ioUrbanTerror
install ioUrTded.x86_64 $RPM_BUILD_ROOT%{_bindir}/ioUrTded
%endif
cp -a q3ut4/*.pk3 $RPM_BUILD_ROOT%{gamedir}/q3ut4
cp -a q3ut4/*.cfg $RPM_BUILD_ROOT%{gamedir}/q3ut4
cp -a q3ut4/{demos,screenshots} $RPM_BUILD_ROOT%{gamedir}/q3ut4

install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/urbanterror
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{gamedir}
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
cp -a %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ioUrbanTerror_id-readme.txt ioUrbanTerror_README.txt
%doc q3ut4/*.txt q3ut4/*.doc
%attr(755,root,root) %{_bindir}/urbanterror
%attr(755,root,root) %{_bindir}/ioUrTded
%attr(755,root,root) %{_bindir}/ioUrbanTerror
%{gamedir}/urbanterror.autodlrc
%{_desktopdir}/urbanterror.desktop
%{_pixmapsdir}/urbanterror.png
%{gamedir}/q3ut4
