# influxdb_grafana
Sample influxdb + grafana dashboard setup in a declarative manner

The python script sends a random value to InfluxDB every 5 seconds and grafana shows the plot.

The influxdb datasource and dashboards have been pre-defined and the files are mounted as a volume inside the grafana container.

You can simply run the docker-compose file provided and go to `http://localhost:3000` to see the dashboard.

## Default Credentials

#### Grafana
- Username: `admin`
- Password: `admin123`

### InfluxDB
- Username: `admin`
- Password: `admin123`
- Database: `testdb`
- Measurement: `sample_measurement`
- Fields: `value`

Yeah I know, don't use shitty passwords. This is a sample blueprint of sorts.
