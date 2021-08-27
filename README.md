<h1> Audsteg </h1>
<b><i>Simple audio cryptography tool</i></b>

Nitya, Mahendra, Anand, Kushagra, Shoab, and Syam are the creators of this project.<br>
Audsteg turns an audio file into encrypted text and then decrypts the encrypted text, returning the original audio as output.

<h1> Steps to work: </h1>

```markdown
pip3 install cryptography
git clone https://github.com/d8rkmind/Audsteg.git

cd Audsteg
python3 Audsteg.py
```markdown

 <h2> Audspy </h2>
 
 
<b></i>Simple audio steganography tool<b></i>

Audspy will hide the plain text inside the given audiofile.

<h2> Hidding using Audspy: </h2>

```markdown
Audspy_hid.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]
```markdown

option|usage
------|-----
 -f | to specify the intial audiofile
 -m | for the secrete message to be hidden inside
 -o | name of the output file
 
 <h2> Extracting using Audspy: </h2>
 
 ```markdown
 Audspy_ext.py [-h] [-f AUDIOFILE]
 ```markdown
 -f is to specify the audio file 
