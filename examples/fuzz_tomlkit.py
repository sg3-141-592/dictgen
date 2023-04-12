import tomlkit
import dictgen

for i in range(10):
    test_data = dictgen.generate(
        key_generators=(
            dictgen.random_string,
        ),
        val_generators=(
            dictgen.random_string,
            dictgen.random_bool,
            dictgen.random_int,
            dictgen.random_datetime
        ),
        nested_generators=(
            dictgen.random_dict,
            dictgen.random_array
        ),
        rand_seed=i
    )

    print(f"Test {i} -------------")
    print(f"test_data: {test_data}")

    try:
        result = tomlkit.dumps(test_data)
        print(f"""result:
{result}
        """)
    except Exception as e:
        print(f"Seed {i}: {e}")
        import json
        print(json.dumps(test_data))
