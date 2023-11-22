"""Titanpy main class used for API access utilyzing the Request library.

This class has a method for every type of API request. Currently only the
Connect() and Get() methods function properly. 

Typical usage example:

    tp = Titanpy("credential/path/string")
    data = tp.Get("endpoint", {query})

Methods:

    Connect()
    Get()
"""
class Titanpy:
    """Titanpy main class used for API access utilyzing the Request library."""
    
    def __init__(self, 
                 credential_path: str
    ):
        """Initializes Servicetitan credentials for Connect method
        
        Args:
            credential_path: Takes "path/as/a/string" in order to verify them through
                servicetitan endpoint.

        """
        from Titanpy.connect import load_credentials

        self.credential_path = credential_path
        credentials = load_credentials(self.credential_path)
        self.set_credentials(credentials["CLIENT_ID"],
                            credentials["CLIENT_SECRET"],
                            credentials["APP_ID"],
                            credentials["APP_KEY"],
                            credentials["TENANT_ID"],
                            credentials["TIMEZONE"],
                            credentials["ACCESS_TOKEN"],
                            credentials
                            )

    def set_credentials(self, 
                    client_id, 
                    client_secret, 
                    app_id, app_key, 
                    tenant_id, 
                    timezone,
                    access_token,
                    credentials
        ):
            """Setter for Servicetitan credentials."""

            self.client_id = client_id
            self.client_secret = client_secret
            self.app_id = app_id
            self.app_key = app_key
            self.tenant_id = tenant_id
            self.timezone = timezone
            self.access_token = access_token
            self.credentials = credentials

    def Get(self, endpoint=None, query = None, id=None, category=None, url=None):
        """Returns data from a source. Must initialize connection in Titanpy class.
        
        Returns request object from either a servicetitan endpoint or a servicetitan
        url. Will accept any valid query that servicetitan endpoints accept. If the
        endpoint required an id or a category in the url, they must be entered as
        arguments, unless a url is used rather than an endpoint. A list of endpoints
        can be found in the readme for this project.

        Args:
            endpoint: Defaults to None. If not None, will search through all programmed
                handlers to find how the endpoint should be requested.
            query: Accepts a dictionary, parameters vary between endpoints.
            id: If the endpoint requires an id in the URL, then the it may be
                entered as an argument.
            category: If the endpoint requires a category, which is defined in
                the documentation README.MD, then it may be entered as an argument/
            url: Defaults to None. If endpoint is None, the url will be used to manually
                query the endpoint. Urls are defined in the servicetitan api documentation.

        Links:
            Servicetitan API Docs: https://developer.servicetitan.io/apis/
        """

        if self.access_token == None:
            print("No proper connection. Please ensure Connect method has been run successfully.")
        elif endpoint !=None:
            from Titanpy.get import get
            print(f"Endpoint received. Requesting for endpoint ({endpoint})")
            return get(credentials = self.credentials, endpoint = endpoint, query = query, id=id, category=category)
        elif url !=None:
            from Titanpy.get import get_request
            print(f"Url received. Requesting from url ({url}).")
            return get_request(credentials = self.credentials, query=query, url=url)
        else:
            print("No endpoint or url has been entered. Please enter an endpoint or a url.")

    def Post(self):  # TODO: https://github.com/pabboat/Titanpy/issues/4 - Create Post handler script in Titanpy/post.py

        if self.access_token == None:
            print("No proper connection. Please ensure Connect method has been run successfully.")

        else:
            print("This method has not been coded yet. See https://github.com/pabboat/Titanpy for more information.")

    def Del(self): # TODO: https://github.com/pabboat/Titanpy - Create Del handler script in Titanpy/post.py

        if self.access_token == None:
            print("No proper connection. Please ensure Connect method has been run successfully.")

        else:
            print("This method has not been coded yet. See https://github.com/pabboat/Titanpy for more information.")

    def Put(self): # TODO: https://github.com/pabboat/Titanpy - Create Put handler script in Titanpy/post.py

        if self.access_token == None:
            print("No proper connection. Please ensure Connect method has been run successfully.")

        else:
            print("This method has not been coded yet. See https://github.com/pabboat/Titanpy for more information.")

    def Patch(self): # TODO: https://github.com/pabboat/Titanpy - Create Patch handler script in Titanpy/post.py

        if self.access_token == None:
            print("No proper connection. Please ensure Connect method has been run successfully.")

        else:
            print("This method has not been coded yet. See https://github.com/pabboat/Titanpy for more information.")


