## πκΈ°μμ²­ λ¨κΈ°μλ³΄ μ‘°νμλΉμ€

###2. μ΄λ¨κΈ°μλ³΄μ‘°ν

**β μμΈκΈ°λ₯ μ€λͺ**: μ΄λ¨κΈ°μλ³΄μ λ³΄λ₯Ό μ‘°ννκΈ° μν΄ λ°νμΌμ, λ°νμκ°, μλ³΄μ§μ  X μ’ν, μλ³΄μ§μ  Y μ’νμ μ‘°ν μ‘°κ±΄μΌλ‘ μλ£κ΅¬λΆμ½λ, μλ³΄κ°, λ°νμΌμ, λ°νμκ°, μλ³΄μ§μ  X μ’ν, μλ³΄μ§μ  Y μ’νμ μ λ³΄λ₯Ό μ‘°ννλ κΈ°λ₯

> #### β­ν΄λΉ μκ°μΌλ‘λΆν° 6μκ° μ΄λ΄κΉμ§μ μ λ³΄λ₯Ό 1μκ° λ¨μλ‘ μ κ³΅β­οΈ

**β οΈκ°±μ  μκ°**: λ§€μκ° 30λΆμ μμ±λκ³  10λΆλ§λ€ μ΅μ  μ λ³΄λ‘ μλ°μ΄νΈ(κΈ°μ¨, μ΅λ, λ°λ)

![img.png](img.png)

**β οΈμ κ³΅ μ λ³΄**:

![img_1.png](img_1.png)

- νλμν(SKY) μ½λ : λ§μ(1), κ΅¬λ¦λ§μ(3), νλ¦Ό(4)
- κ°μνν(PTY) μ½λ : (μ΄λ¨κΈ°) μμ(0), λΉ(1), λΉ/λ(2), λ(3), λΉλ°©μΈ(5), λΉλ°©μΈλλ λ¦Ό(6), λλ λ¦Ό(7) 
                      (λ¨κΈ°) μμ(0), λΉ(1), λΉ/λ(2), λ(3), μλκΈ°(4) 
- λλ’°(LGT) : μλμ§λ°λ(0.2~100KA(ν¬λ‘μνμ΄)/γ’)

![img_2.png](img_2.png)


**β οΈμμ**

```python
{
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "NORMAL_SERVICE"
        },
        "body": {
            "dataType": "JSON",
            "items": {
                "item": [
                    {
                        "baseDate": "20220803",  # λ°ν μΌμ
                        "baseTime": "1230",  # λ°ν μκ°
                        "category": "LGT",  # λλ’°
                        "fcstDate": "20220803",  # μμΈ‘ μΌμ
                        "fcstTime": "1300",  # μμΈ‘ μκ° - 13μ (1μκ° ν)
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "LGT",  # λλ’°
                        "fcstDate": "20220803",
                        "fcstTime": "1400",  # μμΈ‘ μκ° - 14μ (2μκ° ν)
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "LGT",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",  # μμΈ‘ μκ° - 15μ (3μκ° ν)
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "LGT",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",  # μμΈ‘ μκ° - 16μ (4μκ° ν)
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "LGT",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",  # μμΈ‘ μκ° - 17μ (5μκ° ν)
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "LGT",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",  # μμΈ‘ μκ° - 18μ (6μκ° ν)
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "PTY",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "PTY",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "PTY",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "PTY",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "PTY",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "PTY",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "0",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "RN1",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "κ°μμμ",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "RN1",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "κ°μμμ",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "RN1",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "κ°μμμ",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "RN1",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "κ°μμμ",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "RN1",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "κ°μμμ",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "RN1",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "κ°μμμ",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "SKY",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "4",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "SKY",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "4",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "SKY",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "4",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "SKY",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "4",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "SKY",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "4",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "SKY",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "4",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "T1H",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "29",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "T1H",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "29",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "T1H",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "29",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "T1H",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "30",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "T1H",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "30",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "T1H",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "29",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "REH",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "85",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "REH",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "85",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "REH",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "75",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "REH",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "80",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "REH",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "80",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "REH",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "80",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "UUU",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "1.6",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "UUU",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "2",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "UUU",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "2.5",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "UUU",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "3",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "UUU",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "3.1",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "UUU",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "2.8",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VVV",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "0.9",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VVV",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "0.9",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VVV",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "1.1",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VVV",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "1.2",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VVV",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "1.1",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VVV",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "1",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VEC",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "242",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VEC",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "245",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VEC",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "247",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VEC",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "249",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VEC",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "251",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "VEC",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "250",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "WSD",
                        "fcstDate": "20220803",
                        "fcstTime": "1300",
                        "fcstValue": "2",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "WSD",
                        "fcstDate": "20220803",
                        "fcstTime": "1400",
                        "fcstValue": "2",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "WSD",
                        "fcstDate": "20220803",
                        "fcstTime": "1500",
                        "fcstValue": "3",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "WSD",
                        "fcstDate": "20220803",
                        "fcstTime": "1600",
                        "fcstValue": "3",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "WSD",
                        "fcstDate": "20220803",
                        "fcstTime": "1700",
                        "fcstValue": "3",
                        "nx": 60,
                        "ny": 127
                    },
                    {
                        "baseDate": "20220803",
                        "baseTime": "1230",
                        "category": "WSD",
                        "fcstDate": "20220803",
                        "fcstTime": "1800",
                        "fcstValue": "3",
                        "nx": 60,
                        "ny": 127
                    }
                ]
            },
            "pageNo": 1,
            "numOfRows": 1000,
            "totalCount": 60
        }
    }
}
```