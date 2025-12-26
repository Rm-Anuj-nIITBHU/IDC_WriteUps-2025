# All hail Agartha

Desc

**Author** - SEXA

**Points** - 100

### Files provided:
- [https://daily.iitbhucybersec.in/files/agartha/kirk.zip](https://daily.iitbhucybersec.in/files/agartha/kirk.zip) Link to the zip file `kirk.zip` 

### Analysing the files
We download the archived file and extract it giviing us `kirk.png` and the folder `__MACOSX` which is an extra folder that IOS creates while compressing files indicating that is was created on an Apple product and the creator was rich.

We try to open the image `kirk.png` but it turns out to be a corrupt image file indicating that it is not really a PNG file but something else instead.

We then use the `head` and `tail` commands to check its binary data
```bash
$ head kirk.png
```
Output:
```
�
 �������ܧiܧi��S���i
                   <�"k���EBIӚCG�
�N/mnt/challengV�#�KrEݙ�g�]*j@
                              ��i
�!�  F ={��
           ����!#%�o��u��jW_�Wx"$�o�����Ɨ������	�
�
 �
������������������� 
```


## Solution Walkthrough

**Step One** - 

**Step Two** - 

### Final flag : 
`IDC{Flag}`

## Key Concepts

- point1
- point2