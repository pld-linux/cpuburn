Summary:	CPU maximum load (heat) stability test
Summary(pl.UTF-8):   Testy stabilności przy maksymalnym obciążeniu procesora
Name:		cpuburn
Version:	1.4
Release:	3
License:	GPL v2
Group:		Applications
Source0:	http://pages.sbcglobal.net/redelm/%{name}_1_4_tar.gz
# Source0-md5:	f9bb5ff68afb6ccfca11718c90bcab68
Patch0:		%{name}-makefile.patch
URL:		http://pages.sbcglobal.net/redelm/
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

%description -l pl.UTF-8
cpuburn jest zestawem napisanych w asemblerze zadań stworzonych, aby
stworzyć największe możliwe obciążenie cieplne dla procesora oraz
komponentów płyty głównej, poprzez mieszankę instrukcji FPU i ALU
zoptymalizowanych pod P6/P5/K6/K7. Są także zadania do testowania
kontrolerów pamięci RAM (burnMMX/BX). Proszę mieć na uwadze, że
program został stworzony, aby bardzo mocno obciążać kości. Słabo
chłodzone, przetaktowane lub w inny sposób słabe systemy mogą nie
przeżyć testów, powodując straty danych (popsuty system plików), a
także trwałe uszkodzenia sprzętu. Używasz na własne ryzyko!!

%prep
%setup  -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
