SRCDIR := $(shell pwd)
NAME := $(shell basename $(SRCDIR))
include ../common/Makefile

el5:
	rpmbuild $(RPMDEFINES) $(SRCDEFINES) -bs $(NAME)-el.spec --define 'dist .el5.remi' --define 'rhel 5'

el6:
	rpmbuild $(RPMDEFINES) $(SRCDEFINES) -bs $(NAME)-el.spec --define 'dist .el6.remi' --define 'rhel 6'

el7:
	rpmbuild $(RPMDEFINES) $(SRCDEFINES) -bs $(NAME)-el.spec --define 'dist .el7.remi' --define 'rhel 7'

f22:
	rpmbuild $(RPMDEFINES) $(SRCDEFINES) -bs $(NAME).spec --define 'dist .f22.remi' --define 'fedora 22'

f21:
	rpmbuild $(RPMDEFINES) $(SRCDEFINES) -bs $(NAME).spec --define 'dist .f21.remi' --define 'fedora 21'

f20:
	rpmbuild $(RPMDEFINES) $(SRCDEFINES) -bs $(NAME).spec --define 'dist .f20.remi' --define 'fedora 20'

f19:
	rpmbuild $(RPMDEFINES) $(SRCDEFINES) -bs $(NAME).spec --define 'dist .f19.remi' --define 'fedora 19'
