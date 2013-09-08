Name:          jzmq
Version:       2.1.0
Release:       1.oraclejdk7%{?dist}
Summary:       The Java ZeroMQ bindings
Group:         Applications/Internet
License:       LGPLv3+
URL:           http://www.zeromq.org/
Source:        http://www.zeromq.org/local--files/area:download/%{name}-%{version}.tar.gz
Prefix:        %{_prefix}
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++, libstdc++-devel, jdk >= 1.7.0 , zeromq-devel = 2.1.7
Requires:      libstdc++, zeromq, jdk >= 1.7.0, zeromq = 2.1.7

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the Java Bindings for ZeroMQ.

%package devel
Summary:  Development files and static library for the Java Bindings for the ZeroMQ library.
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains Java Bindings for ZeroMQ related development libraries and header files.

%prep
%setup -q

%build
export JAVA_HOME=/usr/java/default
./autogen.sh
%configure

%{__make} -j1

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Install the package to build area
%makeinstall

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)

# docs in the main package
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS README

# libraries
%{_libdir}/libjzmq.so*
/usr/share/java/zmq.jar

%files devel
%defattr(-,root,root,-)
%{_libdir}/libjzmq.la
%{_libdir}/libjzmq.a

%changelog
* Sun Sep 08 2013 Daya Sakti <mr_sakti_9@yahoo.com>
- calls autogen and setup JAVA_HOME prior to calling %configure
- make to run with single job. parallel jobs seem to fail
* Thu Dec 09 2010 Alois Belaska <alois.belaska@gmail.com>
- version of package changed to 2.1.0
* Tue Sep 21 2010 Stefan Majer <stefan.majer@gmail.com> 
- Initial packaging
