# Data model
## Block Class
### The Block class represents a block that contains one or more probes. It contains the following attributes:

- ```id: an integer that serves as the primary key for the Block table. It is set to autoincrement by default.```
- ```name: a string that represents the name of the block. It is required and cannot be null.```

##### The Block class also defines a one-to-many relationship with the Probe class, where each Block may contain multiple probes. This relationship is established using the probes attribute. The backref parameter is set to 'probes', which means that the Probe class will have a block attribute that will allow accessing the corresponding Block object. Finally, the Block class sets up cascade delete for the Probe table when a Block is deleted to delete all associated probes. This is done using the cascade parameter of the relationship function, which is set to 'all, delete-orphan'.

## Probe Class
### The Probe class represents a sensor probe that belongs to a block. It contains the following attributes:

- ```id: an integer that serves as the primary key for the Probe table. It is set to autoincrement by default.```
-```name: a string that represents the name of the probe. It is required and cannot be null.```
-```functional: a boolean that indicates whether the probe is functional or not. It is required and has a default value of True.```
-```block_id: an integer that serves as a foreign key for the Block table. It is required and cannot be null.```

##### The Probe class also defines a one-to-many relationship with the Data class, where each Probe may have multiple data measurements. The backref parameter is set to 'data', which means that the Data class will have a probe attribute that will allow accessing the corresponding Probe object. Finally, when a probe is deleted, all associated data measurements are also deleted. This is done using the cascade parameter of the relationship function, which is set to 'all, delete-orphan'.

## Data Class
### The Data class represents a data measurement for a specific probe. It contains the following attributes:

- ```id: an integer that serves as the primary key for the Data table. It is set to autoincrement by default.```
-```probe_id: an integer that serves as a foreign key for the Probe table. It is required and cannot be null.```
-```timestamp: a string that represents the timestamp of the measurement.```
-```measurement: a float that represents the actual measurement value.```

## Error Class
### The Error class represents an error in a specific probe. It contains the following attributes:

- ```id: an integer that serves as the primary key for the Error table. It is set to autoincrement by default.```
-```probe_id: an integer that serves as a foreign key for the Probe table. It is required and cannot be null.```
-```time_of_error: a string that represents the timestamp of the error.```

## Endpoints
# All the necessary information relating to the endpoints is in the schema and FastAPI docs