# quizlet-converter

## Introduction
A converter to convert a the format into Quizlet format.

Input
```text
落價 lo̍h-kè	降價
落眠 lo̍h-bîn    熟睡
攄頭毛 lu thâu-mn̂g	把頭髮推(剪)平
兩蕊目睭 nn̄g lúi ba̍k-chiu	兩隻眼睛
マスコミ    大眾傳媒、媒體、傳媒業
```

Output
```text
落價(降價),lo̍h-kè
落眠(熟睡),lo̍h-bîn
攄頭毛(把頭髮推(剪)平),lu thâu-mn̂g 
兩蕊目睭(兩隻眼睛),nn̄g lúi ba̍k-chiu 
(大眾傳媒、媒體、傳媒業),マスコミ
```


## Usage
1. Download the file
2. Run the following command in the terminal:
```bash
python3 converter.py <input_file>

# for example
python3 converter.py test.txt
```
3. The output will be in the same directory named as `{file_base_name}-converted.txt`. For example, `test-converted.txt`.
