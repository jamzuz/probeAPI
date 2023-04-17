## Schema

### Block table

| Column Name | Data Type              | Constraints                 |
|-------------|-----------------------|-----------------------------|
| id          | integer               | Primary Key, Autoincrement |
| name        | text                  |                             |

### Probe table

| Column Name | Data Type              | Constraints                       |
|-------------|-----------------------|-----------------------------------|
| id          | integer               | Primary Key, Autoincrement       |
| block_id    | integer               | Foreign Key, references Block(id) |
| name        | text                  |                                   |
| status      | integer               |                                   |

### Reading table

| Column Name | Data Type               | Constraints                       |
|-------------|------------------------|-----------------------------------|
| id          | integer                | Primary Key, Autoincrement        |
| probe_id    | integer                | Foreign Key, references Probe(id) |
| temperature | real                   |                                   |
| timestamp   | timestamp with timezone |                                   |

## Endpoints

### Retrieve all blocks

GET /blocks

Returns a JSON array of objects, where each object represents a block:

```json
[
    {
        "id": 1,
        "name": "Block 1"
    },
    {
        "id": 2,
        "name": "Block 2"
    }
]
```
### Retrieve a single block

GET /blocks/{block_id}

Returns a JSON object representing a single block:

```json
{
    "id": 1,
    "name": "Block 1",
    "probes": [
        {
            "id": 1,
            "name": "Probe 1",
            "temperature": 23.4,
            "status": "ok"
        },
        {
            "id": 2,
            "name": "Probe 2",
            "temperature": null,
            "status": "error"
        }
    ]
}
```

### Retrieve all probes in a block
GET /blocks/{block_id}/probes

Returns a JSON array of objects, where each object represents a probe in the specified block:

```json
[
    {
        "id": 1,
        "name": "Probe 1",
        "temperature": 23.4,
        "status": "ok"
    },
    {
        "id": 2,
        "name": "Probe 2",
        "temperature": null,
        "status": "error"
    }
]
```

### Retrieve a single probe
GET /blocks/{block_id}/probes/{probe_id}

Returns a JSON object representing a single probe:
```json
[
    {
        "id": 1,
        "name": "Probe 1",
        "temperature": 23.4,
        "status": "ok"
    }
]
```