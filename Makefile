# Nama file instalasi
INSTALL_SCRIPT = install.sh

# Nama file utama
MAIN_SCRIPT = secret.py

# Target default
all: install

# Target untuk menjalankan instalasi
install:
	@echo "Menjalankan instalasi tools..."
	@chmod +x $(INSTALL_SCRIPT)
	@./$(INSTALL_SCRIPT)
	@rm -f $(MAIN_SCRIPT)
	@echo "Instalasi selesai. Tools siap digunakan."

# Target untuk membersihkan file sementara jika ada
clean:
	@echo "Membersihkan file sementara..."
	@rm -rf __pycache__

# Target untuk menghapus semua file sementara dan symlink
distclean: clean
	@echo "Menghapus symlink dari tools..."
	@rm -f ~/bin/secret

# Target untuk menjalankan seluruh proses
deploy: install
	@echo "Tools berhasil di-deploy."