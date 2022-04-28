import os
from google.api_core.client_options import ClientOptions
from google.cloud import bigquery
from google.cloud import bigquery_storage
from pathlib import Path
from glob import glob

base_path = Path(__file__).parent
secrets_path = (base_path / "../secrets").resolve()
project_name = 'showvik-argolis-test-project'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = glob(str(secrets_path) + "/*.json")[0]