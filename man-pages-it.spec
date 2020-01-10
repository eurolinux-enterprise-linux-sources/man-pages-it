Summary: Italian man (manual) pages from the Linux Documentation Project
Name: man-pages-it
Version: 3.15
Release: 1%{?dist}
# inherit the license tags from the man-pages package
License: GPL+ and GPLv2 and GPLv2+ and LGPLV2+ and GPLv3+ and BSD and MIT and Copyright only and IEEE
Group: Documentation
URL: http://www.pluto.linux.it/ildp/man/
%define extra_name %{name}-extra
%define extra_ver 0.5.0
# The tarball of the new 3.15 version has a slighly strange file name, not
# %{name}-%{version}.tar.gz anymore ...
Source0: ftp://ftp.pluto.it/pub/pluto/ildp/man/manpages%{version}.tar.bz2
BuildArch: noarch
Obsoletes: %{extra_name} < 2.80
Provides: %{extra_name} = %{version}-%{release}
Summary(it): Pagine del manuale in italiano
%if 0%{?fedora} >= 13
Requires: man-pages-reader
%else
Requires: man
%endif

%description
Manual pages from the Linux Documentation Project, translated into Italian.

%description -l it
Questo pacchetto è la traduzione a cura dell'Italian Linux Documentation
Project (ILDP) del pacchetto man page ufficiale mantenuto e distribuito da
Michael Kerrisk. La versione di questo pacchetto garantisce che le man page
contenute sono state aggiornate alla versione corrispondente del pacchetto
ufficiale. 

%prep
%setup -q
#%patch0 -p1

for i in *; do
    if [ -f $i ]; then
        iconv -f ISO8859-15 -t UTF-8 $i -o $i.utf8
        %__mv $i.utf8 $i
    fi
done
for i in man*/*; do
    if [ -f $i ]; then
        iconv -f ISO8859-15 -t UTF-8 $i -o $i.utf8
        %__mv $i.utf8 $i
    fi
done

%build


%install
%__make prefix=$RPM_BUILD_ROOT
%__mkdir -p $RPM_BUILD_ROOT/%{_mandir}/it
%__cp -R man* $RPM_BUILD_ROOT/%{_mandir}/it
%__rm -rf $RPM_BUILD_ROOT/%{_mandir}/it/'man??'
%__rm -rf $RPM_BUILD_ROOT/share/man
%__rm -f $RPM_BUILD_ROOT/%{_mandir}/it/man1/man2html.1*
%__rm -f $RPM_BUILD_ROOT/%{_mandir}/it/man1/hman.1*


%files
%defattr(-,root,root,-)
%doc CHANGELOG HOWTOHELP POSIX-COPYRIGHT readme
%{_mandir}/it/man*/*


%changelog
* Wed Jan 30 2013 Mike FABIAN <mfabian@redhat.com> - 3.15-1
- Resolves: #906215 - man-pages-it package contains many man-pages
  which are not translated to Italian but are in English
- update to 3.15. The update contains:
- all the man pages from the sections man0p, man1p, and man3p are gone.
  But that is no problem, these were the untranslated English versions anyway!
- new manpages: abc2abc.1 abc2ly.1 abcqps.1 dselect.1 utmpx.5
- removed manpages: dselect.8

* Mon Nov 26 2012 Jens Petersen <petersen@redhat.com> - 2.80-13
- inherit the license tags of the man-pages package (#880076)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.80-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Ding-Yi Chen <dchen@redhat.com> - 2.80-11
- Remove hman.1 as well.

* Tue May 29 2012 Ding-Yi Chen <dchen@redhat.com> - 2.80-10
- Resolves: #825918 - man-pages-it : Conflicts with man2html

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.80-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.80-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 04 2010 Ding-Yi Chen <dchen@redhat.com> - 2.80-7
- Bug 582912 - man-pages-it: Change requires tag from man to man-pages-reader

* Wed Mar 03 2010 Ding-Yi Chen <dchen@redhat.com> - 2.80-6
- Resolves: #560507 [man-pages-it] Package wrangler fix

* Wed Mar 03 2010 Ding-Yi Chen <dchen@redhat.com> - 2.80-5
- Resolves: #560507 [man-pages-it] Package wrangler fix
- Fixed Fedora 569443 [man-pages-it] Wrong directory ownership

* Mon Feb 01 2010 Ding-Yi Chen <dchen@redhat.com> - 2.80-4
- Resolves: #560507
  [man-pages-it] Package wrangler fix
- Remove comments of extra subpackage, as upstream already merge them.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.80-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 26 2008 Ding-Yi Chen <dchen@redhat.com> - 2.80-1
- [Bug 451982] New: RFE: New version of man-pages-it available
- Obsoletes man-pages-it-extra

* Thu Dec 06 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-7
- [Bug 226125] Merge Review: man-page-it (Comment 13)

* Thu Dec 06 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-6
- [Bug 226125] Merge Review: man-page-it (Comment 8)

* Thu Dec 06 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-5
- Fix improper format of SPEC

* Wed Dec 05 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-4
- Change the Licence from "Freely redistributable without restriction" to IEEE

* Tue Dec 04 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-3
- [Bug 226125] Merge Review: man-page-it

* Thu Oct 25 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-2
- [Bug 335931] man-pages-it package is 6 years old
- Add Italian summaries and descriptions

* Mon Oct 22 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-0
- [Bug 335931] man-pages-it package is 6 years old

* Wed Oct 10 2007 Ding-Yi Chen <dchen@redhat.com> - 0.3.0-18
- [Bug 236116] Unsupported programs in man-pages-it
- remove celibacy.1 and sex.6

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-17.1.gz
- rebuild

* Thu Mar 23 2006 Karsten Hopp <karsten@redhat.de> 0.3.0-17
- remove vim.1, provided by the vim-common package

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Apr 07 2005 Peter Vrabec <pvrabec@redhat.com> 0.3.0-16
- newgrp man page removed, will be provided by shadow-utils

* Tue Sep 28 2004 Leon Ho <llch@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 0.3.0-13
- removed apropos.1, man.1, whatis.1, man.config.5, and makewhatis.8, because the latest man contains those manpages.

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 0.3.0-12
- Convert all manpages to utf-8.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.3.0-11
- rebuilt

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 0.3.0-10
- remove unpackaged files from the buildroot

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.3.0-7
- Add URL

* Wed Apr  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add patch to fix roff errors in multiple man pages

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Mon Jun 19 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Sun Jun 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_mandir}/it and %%{_tmppath} 

* Mon May 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first build
