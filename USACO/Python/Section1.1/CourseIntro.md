USA Team site
---
- [USACO](http://usaco.org)
  - [Contests](http://usaco.org/index.php?page=contests)
    - On-Line Contests
    - The Road to the IOI Team
  - [Resources](http://usaco.org/index.php?page=resources)
    - Books about **Competitive Programming**
    
    
Note: pay attention to the challenge schedule on the front page!

International Olympiad in Informatics
---
- [IOI](https://ioinformatics.org/)
- [Wiki](https://en.wikipedia.org/wiki/International_Olympiad_in_Informatics)

International Collegiate Programming Contest
---
- [ICPC](https://icpc.global/)


USACO Training Gateway
---
https://train.usaco.org/
- All submission must have a comment block with following contents
 - LANG:
 - TASK:

### Submission
#### Please be noted that these lines should not contain any other characters, including '*'

- All input/output files are named exactly after TASK keyword:
 - **\<task name\>.in**
 - **\<task name\>.out**
- For output file, must have a '\\n' at the last line

#### Special notes for Java programmer:
- USACO does not expect any "package" line on top of your main class. So you have to drop it.

File I/O
---

#### Java
```java
Scanner sc = new Scanner(new File("test.in"));
int x = sc.nextInt();
int y = sc.nextInt();

FileWriter fw = new FileWriter("test.out");
fw.write( (x+y) + "\n" );
fw.close();
```

#### Python
```python
fin = open('prob.in') 
lst = fin.readlines()

with open('prob.out', 'w') as fout:
    fout.write( '%s\n' % answer )
```

#### C++
```cpp
ifstream fin ("test.in");
int a, b;
fin >> a >> b;

ofstream fout ("test.out");
fout << a+b << endl;
```

Progress Together
---
I'll try following the **average speed**
- Your turn-in rates determine overall progress
- Do not share the complete answer for USACO challenges

Reference Data
---
![](https://upload.wikimedia.org/wikipedia/commons/d/dd/ASCII-Table.svg)
