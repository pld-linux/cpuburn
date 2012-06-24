Summary:	CPU maximum load (heat) stability test
Summary(pl):	Testy stabilno�ci przy maksymalnym obci��eniu procesora
Name:		cpuburn
Version:	1.4
Release:	1
License:	GPL
Group:		Applications
Source0:	http://users.ev1.net/~redelm/%{name}_1_4_tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://users.ev1.net/~redelm/
ExclusiveArch:	i586 i686 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cpuburn is a suite of assembly-coded routines designed to put maximum
heat stress on the CPU and motherboard components by a
P6/P5/K6/K7-optimized mix of FPU and ALU instructions. There are also
routines to test RAM controllers (burnMMX/BX). Please note that this
program is designed to heavily load chips. Undercooled, overclocked,
or otherwise weak systems may fail, causing data loss (filesystem
corruption) and possibly permanent damage to electronic components.
Use it at your own risk!!

%description -l pl
cpuburn jest zestawem napisanych w asemblerze zada� stworzonych, aby
stworzy� najwi�ksze mo�liwe obci��enie cieplne dla procesora oraz
komponent�w p�yty g��wnej, poprzez mieszank� instrukcji FPU i ALU
zoptymizowanych pod P6/P5/K6/K7. S� tak�e zadania do testowania
kontroler�w pami�ci RAM (burnMMX/BX). Prosz� mie� na uwadze, �e
program zosta� stworzony, aby bardzo mocno obci��a� ko�ci. S�abo
ch�odzone, przetaktowane lub w inny spos�b s�abe systemy mog� nie
prze�y� test�w, powoduj�c straty danych (popsuty system plik�w), a
tak�e trwa�e uszkodzenia sprz�tu. U�ywasz na w�asne ryzyko!!

%prep
%setup  -q
%patch0 -p1

%build
%{__make} CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install burn{BX,K6,K7,MMX,P5,P6} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Design README
%attr(754,root,root) %{_sbindir}/*
