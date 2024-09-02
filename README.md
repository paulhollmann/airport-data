# Airport Data

Manages the airport data used on the VATSIM Germany homepage.

### Airport type:

```
[[airport]]
icao = "EDDY"

[[airport.links]]
category = "Scenery" | "Charts" | "Briefing" | NONE
name = "Display Name 1"
url = "https://example.url"
```

example:

```
[[airport]]
icao = "EDDY"

[[airport.links]]
category = "Scenery"
name = "Display Name 1"
url = "https://example.url"

[[airport.links]]
category = "Charts"
name = "Display Name 2"
url = "https://example2.url"

```

# TODO:

- validate data links to not return 404
- give warnings using PRs or Discord hook?
-
