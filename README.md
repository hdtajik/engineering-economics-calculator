# Engineering Economics Calculator

## cfc - compounding factor calculator

### General Syntax

```
python cfc.py <-n period> <-i interest_rate> [-p precision] [--cc]
```

### Usage Example

- _Discrete Compounding_

```
~$ python cfc.py -n 7 -i 0.13 -p 2
Compounding Factor Calculator - Discrete
(F/P, 13.0%, 7.0) = 2.35
(P/F, 13.0%, 7.0) = 0.43
(P/A, 13.0%, 7.0) = 4.42
(A/P, 13.0%, 7.0) = 0.23
(F/A, 13.0%, 7.0) = 10.4
(A/F, 13.0%, 7.0) = 0.1
(P/G, 13.0%, 7.0) = 11.13
(A/G, 13.0%, 7.0) = 2.52
```

- _Continuous Compounding_

```
~$ python cfc.py -n 7 -i 0.13 --cc
Compounding Factor Calculator - Continuous
(F/P, 13.0%, 7.0) = 2.4843
(P/F, 13.0%, 7.0) = 0.4025
(P/A, 13.0%, 7.0) = 4.3037
(A/P, 13.0%, 7.0) = 0.2324
(F/A, 13.0%, 7.0) = 10.6918
(A/F, 13.0%, 7.0) = 0.0935
(P/G, 13.0%, 7.0) = 10.7041
(A/G, 13.0%, 7.0) = 2.4872
```

## clc - a generic calculator

### General Syntax

```
python clc.py <calculation> [-p precision]
```

_compounding factor (X/Y, i%, n) : xy(i, n)_

### Usage Example

- _(3000 (P/A, 8%, 5) - 500 (P/G, 8%, 5)) (P/F, 8%, 3) + 3000 (P/F, 8%, 3)_

```
python clc.py "(3000 * pa(0.08, 5) - 500 * pg(0.08, 5)) * pf(0.08, 3) + 3000 * pf(0.08, 3)"
```

_8963.89_

- _-240000 + 61400 (P/A, 20%, 10) + 60000 (P/F, 20%, 10)_

```
python clc.py "-240000 + 61400 * pa(0.2, 10) + 60000 * pf(0.2, 10)" -p 3
```

_27108.121_

## ror - rate of return calculator

### General Syntax

```
python ror.py <equation> [-u upper_boundary] [-l lower_boundary] [-p precision]
```

_compounding factor (X/Y, i%, n) : xy(i, n)_

### Usage Example

- _-120000 + (29000 - 3000 (A/G, i%, 10)) (P/A, i%, 10) + 12000 (P/F, i%, 10) = 0_

```
python ror.py "-120000 + (29000 - 3000 * ag(i, 10)) * pa(i, 10) + 12000 * pf(i, 10)"
```

_Rate of Return: 8.53%_

- _-240000 + 61400 (P/A, i%, 10) + 60000 (P/F, i%, 10) = 0_

```
python ror.py "-240000 + 61400 * pa(i, 10) + 60000 * pf(i, 10)" -l 23 -u 24 -p 5
```

_Rate of Return: 23.10572%_

## edc - economics depreciation calculator

- Straight Line - **_sl_**
- Sum Of The Years Digits - **_soyd_**
- Declining Balance - **_db_**
- Sinking Fund - **_sf_**
- Unit of Production - **_up_**
- Operation Time - **_ot_**

### General Syntax

```
python edc.py <method_name> <--oc operational_cost> <--sv salvage_value> <-n period> <-i interest_rate>
```

#### Method Specific Arguments

| method | argument |          definition          |
| :----: | :------: | :--------------------------: |
|  _db_  |   _-d_   | depreciation rate (optional) |
|  _up_  |  _--um_  |        produced unit         |
|  _ot_  |  _--qm_  |        operated time         |

### Usage Example

- Straight Line

```
~$ python edc.py sl --oc 3000 --sv 1000 -n 7 -i 0.13
Economics Depreciation Calculator - Straight Line
Year		Depreciation		Book Value
1		285.71			2714.29
2		285.71			2428.57
3		285.71			2142.86
4		285.71			1857.14
5		285.71			1571.43
6		285.71			1285.71
7		285.71			1000.0
Original Cost: 3000.0
Salvage value: 1000.0
No. periods: 7
Interest rate: 13.0%
PW (depreciation): 1263.6
EUA (depreciation): 285.71
```

- Declining Balance

```
~$ python edc.py db --oc 600000 --sv 40000 -n 10 -i 0.1
Economics Depreciation Calculator - Declining Balance
Year		Depreciation		Book Value
1		142340.88		457659.12
2		108572.67		349086.46
3		82815.45		266271.0
4		63168.75		203102.26
5		48182.92		154919.33
6		36752.26		118167.08
7		28033.34		90133.74
8		21382.86		68750.88
9		16310.1		        52440.78
10		12440.78		40000.0
Original Cost: 600000.0
Salvage value: 40000.0
No. periods: 10
Interest rate: 10.0%
PW (depreciation): 411233.68
EUA (depreciation): 66926.39
```

- Unit of Production

```
~$ python edc.py up --oc 1500 --sv 300 -n 5 -i 0.2 --um "[100, 100, 200, 300, 500]"
Economics Depreciation Calculator - Unit of Production
Year		Depreciation		Book Value
1		100.0			1400.0
2		100.0			1300.0
3		200.0			1100.0
4		300.0			800.0
5		500.0			300.0
Original Cost: 1500.0
Salvage value: 300.0
No. periods: 5
Interest rate: 20.0%
PW (depreciation): 614.13
EUA (depreciation): 205.35
```
