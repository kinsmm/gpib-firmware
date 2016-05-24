install:
	for d in agilent_82357a ni_gpib_usb_b; do\
	  mkdir -p "$(DESTDIR)/usr/share/usb/$$d/";\
	  install $$d/*.hex $$d/README\
	          $(DESTDIR)/usr/share/usb/$$d/;\
	done