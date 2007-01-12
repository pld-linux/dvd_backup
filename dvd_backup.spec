Summary:	Backup on DVD
Summary(pl):	Kopie zapasowe na DVD
Name:		dvd_backup
Version:	0.5.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://silvercoders.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	2e8a35213ca0fe7502a9873d32bbba44
URL:		http://silvercoders.com/index.php?page=DVD_Backup
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SILVERCODERS DVD Backup is an unix shell script providing
functionality for backuping files and databases (PostgreSQL, MySQL) on
DVD discs. DVD Backup supports multisession and incremental backups.
Mail notification is also supported.

%description -l pl
SILVERCODERS DVD Backup jest skryptem unixowym s³u¿±cym do robienia
kopii zapasowych plików oraz baz danych (PostgreSQL, MySQL) na p³ytach
DVD. DVD Backup wspiera multisesje oraz kopie przyrostowe.
Powiadamianie na maila jest równie¿ dostêpne.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp dvd_backup.sh $RPM_BUILD_ROOT%{_bindir}/dvd_backup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog dvd_backup.conf.sample
%attr(755,root,root) %{_bindir}/*
