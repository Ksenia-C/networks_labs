# Сохраненные конфигурации

[vpc6](vpc6): 10.0.0.1

[vpc7](vpc7): 20.0.0.1

[vpc5](vpc5): 30.0.0.1

[vyos1](vyos1) - интернет

[vyos2](vyos2) - общий роутер для обоих тунелей

[vyos3](vyos3) - только gre

[vyos4](vyos4) - gre + ipsec

# Сеть
![](img/scheme.jpg)

# default route на пограничных настроен в интернет

![](img/default.jpg)

# В интернете только direct connected

![](img/internet_directed.jpg)

# GRE работает

![](img/gre.jpg)

# GRE + IPSec работает

![](img/gre_ipsec.jpg)
