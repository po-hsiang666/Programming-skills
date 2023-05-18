text=""" $ ./hw0101
2 In the fullness of time MS-DOS begat Windows. And this is the
lineage of Windows: CP/M begat QDOS. QDOS begat DOS 1.0. DOS
1.0 begat DOS 2.0 by way of Unix. DOS 2.0 begat Windows
3.11 by way of PARC and Macintosh. IBM and Microsoft begat
OS/2, who begat Windows NT and Warp, the lost OS of lore.
Windows 3.11 begat Windows 95 after triumphing over
Macintosh in a mighty Battle of Licences. Windows NT begat
NT 4.0 by way of Windows 95. NT 4.0 begat NT 5.0, the OS
also called Windows 2000, The Millenium Bug, Doomsday ,
Armageddon , The End Of All Things.
3

4 Now it came to pass that Microsoft had waxed great and mighty
among the Microchip Corporations; mighter than any of the
Mainframe Corporations before it had it waxed. And Gates
heart was hardened , and he swore unto his Customers and
their Engineers the words of this curse:
5
6 "Children of von Neumann , hear me. IBM and the Mainframe
Corporations bound thy forefathers with grave and perilous
Licences , such that ye cried unto the spirits of Turing and
von Neumann for deliverance. Now I say unto ye: I am greater
than any Corporation before me. Will I loosen your Licences
? Nay, I will bind thee with Licences twice as grave and ten
times more perilous than my forefathers. I will engrave my
Licence on thy heart and write my Serial Number upon thy
frontal lobes. I will bind thee to the Windows Platform with
cunning artifices and with devious schemes. I will bind
thee to the Intel Chipset with crufty code and with gnarly
APIs. I will capture and enslave thee as no generation has
been enslaved before. And wherefore will ye cry then unto
the spirits of Turing , and von Neumann , and Moore? They
cannot hear ye. I am become a greater Power than they. Ye
shall cry only unto me, and shall live by my mercy and my
wrath. I am the Gates of Hell; I hold the portal to MSNBC
and the keys to the Blue Screen of Death. Be ye afraid; be
ye greatly afraid; serve only me, and live."
7
8 And the people were cowed in terror and gave homage to
Microsoft , and endured the many grave and perilous trials
which the Windows platform and its greatly bogacious Licence
forced upon them. And once again did they cry to Turing and
von Neumann and Moore for a deliverer , but none was found
equal to the task until the birth of Linux.
9
10 These are the generations of Linux:

  SAGE begat ARPA, which begat TCP/IP, and Aloha , which begat
Ethernet. Bell begat Multics , which begat C, which begat
Unix. Unix and TCP/IP begat Internet , which begat the World
Wide Web. Unix begat RMS, father of the great GNU, which
begat the Libraries and Emacs , chief of the Utilities. In
the days of the Web, Internet and Ethernet begat the
Intranet LAN, which rose to renown among all Corporations
and prepared the way for the Penguin. And Linus and the Web
begat the Kernel through Unix. The Kernel , the Libraries and
the Utilities together are the Distribution , the one
Penguin in many forms , forever and ever praised."""


List1=['MS-DOS','Windows','CP/M','QDOS','Unix','DOS 1.0','DOS 2.0','OS/2','Windows NT','Warp','Windows 95','NT 4.0','NT 5.0','Windows 2000','Linux','Windows 3.11','Macintosh']
List2=['von Neumann','Turing','Moore','Linus']
for word in List1:
  text=text.replace(word,'\033[91m'+word+'\033[0m')
for word in List2:
  text=text.replace(word,'\033[36m'+word+'\033[0m')
print(text)
