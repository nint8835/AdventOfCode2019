print(
    sorted(
        map(
            lambda i: i[0] + i[1],
            (
                w2 := lambda m, x, y, p: [
                    *(
                        {
                            "U": lambda m: [
                                (x, y_coord)
                                for y_coord in range(y, y + m + 1)
                                if (x, y_coord) in p
                            ],
                            "D": lambda m: [
                                (x, y_coord)
                                for y_coord in range(y - m, y + 1)
                                if (x, y_coord) in p
                            ],
                            "R": lambda m: [
                                (x_coord, y)
                                for x_coord in range(x, x + m + 1)
                                if (x_coord, y) in p
                            ],
                            "L": lambda m: [
                                (x_coord, y)
                                for x_coord in range(x - m, x + 1)
                                if (x_coord, y) in p
                            ],
                        }[m[0][0]](int(m[0][1:]))
                    ),
                    *w2(
                        m[1:],
                        {
                            "U": lambda m: x,
                            "D": lambda m: x,
                            "R": lambda m: x + m,
                            "L": lambda m: x - m,
                        }[m[0][0]](int(m[0][1:])),
                        {
                            "U": lambda m: y + m,
                            "D": lambda m: y - m,
                            "R": lambda m: y,
                            "L": lambda m: y,
                        }[m[0][0]](int(m[0][1:])),
                        p,
                    ),
                ]
                if len(m) != 0
                else []
            )(
                (f := open("i").read().split("\n"))[1].split(","),
                0,
                0,
                (
                    w1 := lambda m, x, y, p: w1(
                        m[1:],
                        {
                            "U": lambda m: x,
                            "D": lambda m: x,
                            "R": lambda m: x + m,
                            "L": lambda m: x - m,
                        }[m[0][0]](int(m[0][1:])),
                        {
                            "U": lambda m: y + m,
                            "D": lambda m: y - m,
                            "R": lambda m: y,
                            "L": lambda m: y,
                        }[m[0][0]](int(m[0][1:])),
                        {
                            **p,
                            **(
                                {
                                    "U": lambda m: {
                                        (x, y_coord): True
                                        for y_coord in range(y, y + m + 1)
                                        if (x, y_coord) != (0, 0)
                                    },
                                    "D": lambda m: {
                                        (x, y_coord): True
                                        for y_coord in range(y - m, y + 1)
                                        if (x, y_coord) != (0, 0)
                                    },
                                    "R": lambda m: {
                                        (x_coord, y): True
                                        for x_coord in range(x, x + m + 1)
                                        if (x_coord, y) != (0, 0)
                                    },
                                    "L": lambda m: {
                                        (x_coord, y): True
                                        for x_coord in range(x - m, x + 1)
                                        if (x_coord, y) != (0, 0)
                                    },
                                }[m[0][0]](int(m[0][1:]))
                            ),
                        },
                    )
                    if len(m) != 0
                    else p
                )(f[0].split(","), 0, 0, {}),
            ),
        )
    )[0]
)