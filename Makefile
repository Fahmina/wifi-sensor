module.tar.gz: exec.sh setup.sh .env src/*.py requirements.txt meta.json
	tar czf $@ $^
