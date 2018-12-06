#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-MQTT
Version  : 1.163170
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/B/BE/BEANZ/Net-MQTT-1.163170.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BE/BEANZ/Net-MQTT-1.163170.tar.gz
Summary  : 'Perl modules for MQTT Protocol (http://mqtt.org/)'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-MQTT-bin = %{version}-%{release}
Requires: perl-Net-MQTT-license = %{version}-%{release}
Requires: perl-Net-MQTT-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Pluggable)

%description
SYNOPSIS
# net-mqtt-sub /topic

# net-mqtt-pub /topic message

# net-mqtt-trace mqtt.tcp

%package bin
Summary: bin components for the perl-Net-MQTT package.
Group: Binaries
Requires: perl-Net-MQTT-license = %{version}-%{release}
Requires: perl-Net-MQTT-man = %{version}-%{release}

%description bin
bin components for the perl-Net-MQTT package.


%package dev
Summary: dev components for the perl-Net-MQTT package.
Group: Development
Requires: perl-Net-MQTT-bin = %{version}-%{release}
Provides: perl-Net-MQTT-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-MQTT package.


%package license
Summary: license components for the perl-Net-MQTT package.
Group: Default

%description license
license components for the perl-Net-MQTT package.


%package man
Summary: man components for the perl-Net-MQTT package.
Group: Default

%description man
man components for the perl-Net-MQTT package.


%prep
%setup -q -n Net-MQTT-1.163170

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-MQTT
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-MQTT/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT.pod
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Constants.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/ConnAck.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/Connect.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/Disconnect.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/JustMessageId.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/PingReq.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/PingResp.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/PubAck.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/PubComp.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/PubRec.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/PubRel.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/Publish.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/SubAck.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/Subscribe.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/UnsubAck.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/Message/Unsubscribe.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/MQTT/TopicStore.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/net-mqtt-pub
/usr/bin/net-mqtt-sub
/usr/bin/net-mqtt-trace

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::MQTT.3
/usr/share/man/man3/Net::MQTT::Constants.3
/usr/share/man/man3/Net::MQTT::Message.3
/usr/share/man/man3/Net::MQTT::Message::ConnAck.3
/usr/share/man/man3/Net::MQTT::Message::Connect.3
/usr/share/man/man3/Net::MQTT::Message::Disconnect.3
/usr/share/man/man3/Net::MQTT::Message::JustMessageId.3
/usr/share/man/man3/Net::MQTT::Message::PingReq.3
/usr/share/man/man3/Net::MQTT::Message::PingResp.3
/usr/share/man/man3/Net::MQTT::Message::PubAck.3
/usr/share/man/man3/Net::MQTT::Message::PubComp.3
/usr/share/man/man3/Net::MQTT::Message::PubRec.3
/usr/share/man/man3/Net::MQTT::Message::PubRel.3
/usr/share/man/man3/Net::MQTT::Message::Publish.3
/usr/share/man/man3/Net::MQTT::Message::SubAck.3
/usr/share/man/man3/Net::MQTT::Message::Subscribe.3
/usr/share/man/man3/Net::MQTT::Message::UnsubAck.3
/usr/share/man/man3/Net::MQTT::Message::Unsubscribe.3
/usr/share/man/man3/Net::MQTT::TopicStore.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-MQTT/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/net-mqtt-pub.1
/usr/share/man/man1/net-mqtt-sub.1
/usr/share/man/man1/net-mqtt-trace.1
