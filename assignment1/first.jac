node Greeter {
    can lovejac {
        return "With Jac, Python becomes even more awesome!";
    }
}

walker main {
    root {
        spawn here ++> Greeter;
        here.lovejac() |> std.out;
    }
}

with entry {
    take --> main;
}
