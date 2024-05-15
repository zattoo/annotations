# Annotations


A GitHub Action that can be used across multiple repositories, for forwarding component release details to Telemetry.


## Inputs

**`component`**

string

Required. Name of the component name

**`date`**

string

Required. Release Published date 

**`version`**

string

Required. Release Version 

**`type`**

string

Required. Release Type

**`tenantId`**

int

Required. TenantId

**`urlProduction`**

string

Required. Provide the endpoints for Zolagus Production

**`urlStaging`**

string

Required. Provide the endpoints for Zolagus Staging


**`Usage Example`**
```yaml
    name: annotations
    steps:
    
     -   name: Call the Action to send the release to endpoints
         uses: zattoo/annotations@main
         with:
          component: ${{env.RELEASE_COMPONENT}}
          date: ${{env.RELEASE_DATE}}
          version: ${{env.RELEASE_TAG}}
          type: ${{env.RELEASE_TYPE}}
          tenantId: ${{env_TenantId}}
          urlProduction: ${{env.URL_PRODUCTION}}
          urlStaging: ${{env.URL_STAGING}}
```
