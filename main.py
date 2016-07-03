#/usr/bin/python
os.system('ls')
os.system('shntool join -o wav *.wav')
os.system('shntool conv flac joined.wav')
os.system('rm -f joined.wav')
os.system('shntool cue *.wav > CDImage.cue')
