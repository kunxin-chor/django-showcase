{"changed":true,"filter":false,"title":"models.py","tooltip":"/todos/models.py","value":"from django.db import models\n\n# Create your models here.\n\n# declare a class named \"Item\"\nclass Item(models.Model):\n    name = models.CharField(max_length=30, blank=False)\n    done = models.BooleanField(blank=False, default=False)\n    \n","undoManager":{"mark":36,"position":42,"stack":[[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["c"],"id":2},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["l"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["a"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["s"]},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":[" "],"id":3},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["I"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["t"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["e"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":12},"action":"insert","lines":["()"],"id":4}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["m"],"id":5},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["o"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["d"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["e"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["l"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["s"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["."]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["M"],"id":6},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["o"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["d"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["e"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["l"]}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":[":"],"id":7}],[{"start":{"row":2,"column":26},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":[" "],"id":9},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["d"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["e"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["c"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["l"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["a"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["r"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":[" "],"id":10},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["a"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":[" "],"id":11},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["c"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["l"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["a"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["s"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":[" "],"id":12},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["n"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["a"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["m"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["e"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":[" "],"id":13}],[{"start":{"row":4,"column":24},"end":{"row":4,"column":26},"action":"insert","lines":["\"\""],"id":14}],[{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["I"],"id":15},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["t"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["e"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["m"]}],[{"start":{"row":5,"column":25},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["n"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["a"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["m"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":[" "],"id":17},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":[" "],"id":18},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["m"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["o"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["d"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["e"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["l"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["."],"id":19},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["C"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["h"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["a"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["r"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["F"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["i"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["e"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["l"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":29},"action":"insert","lines":["()"],"id":20}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["m"],"id":21},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["a"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["x"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["_"]}],[{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["l"],"id":22},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["e"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["n"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["g"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["t"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["h"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["="]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["3"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["0"]}],[{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":[","],"id":23}],[{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":[" "],"id":24},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["b"]},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":["l"]},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"insert","lines":["a"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"insert","lines":["n"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"insert","lines":["k"]},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"insert","lines":["="]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"insert","lines":["F"]},{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"insert","lines":["a"]},{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"insert","lines":["l"]},{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"insert","lines":["s"]},{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":55},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["d"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["o"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["e"],"id":26}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":[" "],"id":27},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":[" "],"id":28},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["m"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["o"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["d"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["e"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["l"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["s"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["."]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["B"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["o"],"id":29},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["l"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["e"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["a"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["n"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["F"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["i"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["e"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["l"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":32},"action":"insert","lines":["()"],"id":30}],[{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["b"],"id":31},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["a"]}],[{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"remove","lines":["a"],"id":32}],[{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["l"],"id":33},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["a"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["k"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"remove","lines":["="],"id":34},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"remove","lines":["k"]}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["n"],"id":35},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["k"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["="]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["F"]},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["a"]},{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["l"]},{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["s"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":[","],"id":36}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":[" "],"id":37},{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["d"]},{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["e"]},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["f"]},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["a"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["u"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["l"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["t"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":["F"],"id":38},{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"insert","lines":["a"]},{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"insert","lines":["l"]},{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"insert","lines":["s"]},{"start":{"row":7,"column":56},"end":{"row":7,"column":57},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["I"],"id":39}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["i"],"id":40}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["i"],"id":41}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["I"],"id":42}],[{"start":{"row":7,"column":58},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":46}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":0},"end":{"row":9,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565079768475}