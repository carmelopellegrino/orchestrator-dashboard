CONFIGURATION_PROFILE = "default"

### IAM SETTINGS
IAM_CLIENT_ID = "XXX-XXX-XXX-XXX-XXX"
IAM_CLIENT_SECRET = "************"
IAM_BASE_URL = "https://iam.example.com"
ORCHESTRATOR_URL = "https://orchestrator.example.com"
CALLBACK_URL = "https://dashboard.example.com/home/callback"

### TOSCA-related SETTINGS
TOSCA_TEMPLATES_DIR = "/opt/tosca-templates"
TOSCA_PARAMETERS_DIR = "/opt/tosca-parameters"
TOSCA_METADATA_DIR = "/opt/tosca-metadata"

### DB SETTINGS
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dashboard:dashboard@localhost/orchestrator_dashboard",
SQLALCHEMY_TRACK_MODIFICATIONS = "False"
SQLALCHEMY_VERSION_HEAD = "88bc3c2c02a6"

### NOTIFICATION SETTINGS
MAIL_SERVER = "relay-mbox.recas.ba.infn.it"
MAIL_PORT = "25"
MAIL_DEFAULT_SENDER = "admin@orchestrator-dashboard"
MAIL_USERNAME = None
MAIL_PASSWORD = None


### ADMIN SETTINGS
SUPPORT_EMAIL = "marica.antonacci@ba.infn.it"
ADMINS = "['marica.antonacci@ba.infn.it']"
EXTERNAL_LINKS = []
OVERALL_TIMEOUT = 720
PROVIDER_TIMEOUT = 720
LOG_LEVEL = "info"
UPLOAD_FOLDER = "/tmp"

FEATURE_ADVANCED_MENU = "no"
FEATURE_UPDATE_DEPLOYMENT = "no"
FEATURE_HIDDEN_DEPLOYMENT_COLUMNS = "4, 5, 7"
FEATURE_VAULT_INTEGRATION = "no"

### VAULT INTEGRATION SETTINGS
VAULT_ROLE = "orchestrator"
VAULT_OIDC_AUDIENCE = "ff2c57dc-fa09-43c9-984e-9ad8afc3fb56"

#### LOOK AND FEEL SETTINGS
WELCOME_MESSAGE = "Welcome! This is the PaaS Orchestrator Dashboard"
NAVBAR_BRAND_TEXT = "PaaS Orchestrator Dashboard"
NAVBAR_BRAND_ICON = "/home/static/images/orchestrator-logo.png"

### Template Paths
HOME_TEMPLATE = 'home.html'
FOOTER_TEMPLATE = 'footer.html'