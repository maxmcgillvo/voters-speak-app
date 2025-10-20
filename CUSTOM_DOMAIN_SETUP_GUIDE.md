# Custom Domain Setup Guide for voters-speak.com

## Overview
Since you cannot access the name servers directly, we'll configure DNS records at name.com to point to your Netlify site.

## Your Netlify Site Information
- **Netlify Site URL**: https://dreamy-manatee-714bdc.netlify.app/
- **Custom Domain**: www.voters-speak.com
- **Root Domain**: voters-speak.com

## Step 1: Add Custom Domain in Netlify

1. **Log in to Netlify**: https://app.netlify.com
2. **Go to your site**: "dreamy-manatee-714bdc"
3. **Click "Domain settings"** (or "Set up a custom domain")
4. **Click "Add custom domain"**
5. **Enter**: `www.voters-speak.com`
6. **Click "Verify"** and then **"Add domain"**
7. **Also add the root domain**: `voters-speak.com`
   - Netlify will automatically redirect voters-speak.com → www.voters-speak.com

## Step 2: Get Netlify's DNS Information

After adding the custom domain, Netlify will show you DNS configuration instructions. You'll need:

### For www.voters-speak.com (CNAME):
- **Type**: CNAME
- **Name/Host**: www
- **Value/Points to**: dreamy-manatee-714bdc.netlify.app

### For voters-speak.com (Root Domain):
Netlify provides Load Balancer IPs. You'll need to create A records:
- **Type**: A
- **Name/Host**: @ (or leave blank for root)
- **Value/Points to**: One of these Netlify IPs:
  - 75.2.60.5
  - 99.83.190.102
  - 13.248.212.111
  - 76.76.21.21

**Note**: Netlify may show different IPs in your dashboard. Use the ones shown there.

## Step 3: Configure DNS at name.com

1. **Log in to name.com**: https://www.name.com/account/domain
2. **Find voters-speak.com** in your domain list
3. **Click "Manage"** next to the domain
4. **Go to "DNS Records"** section

### Add/Update These Records:

#### Record 1: CNAME for www
```
Type: CNAME
Host: www
Answer: dreamy-manatee-714bdc.netlify.app
TTL: 300 (or Auto)
```

#### Record 2-5: A Records for Root Domain
Add FOUR A records (all pointing to root domain):

```
Type: A
Host: @ (or blank)
Answer: 75.2.60.5
TTL: 300

Type: A
Host: @ (or blank)
Answer: 99.83.190.102
TTL: 300

Type: A
Host: @ (or blank)
Answer: 13.248.212.111
TTL: 300

Type: A
Host: @ (or blank)
Answer: 76.76.21.21
TTL: 300
```

**Important**: 
- Delete any existing A records for @ or www that point elsewhere
- Delete any existing CNAME records for www that point elsewhere
- Keep MX records (email) if you have them

## Step 4: Enable HTTPS in Netlify

1. **Go back to Netlify** → Your site → Domain settings
2. **Scroll to "HTTPS"** section
3. **Click "Verify DNS configuration"**
4. **Wait for verification** (may take a few minutes)
5. **Click "Provision certificate"** once DNS is verified
6. **Enable "Force HTTPS"** to redirect all HTTP traffic to HTTPS

## Step 5: Wait for DNS Propagation

- **Typical wait time**: 5-30 minutes
- **Maximum wait time**: Up to 48 hours (rare)
- **Check status**: Use https://dnschecker.org to verify propagation

## Verification Steps

### Check if DNS is working:
1. Open terminal/command prompt
2. Run: `nslookup www.voters-speak.com`
3. Should show: `dreamy-manatee-714bdc.netlify.app`

### Check if site is accessible:
1. Visit: https://www.voters-speak.com
2. Should load your Voters Speak application
3. Check that HTTPS (padlock) is working

## Troubleshooting

### Issue: "DNS verification failed"
**Solution**: 
- Wait 15-30 minutes for DNS propagation
- Double-check DNS records at name.com
- Make sure you deleted old conflicting records

### Issue: "Certificate provisioning failed"
**Solution**:
- Verify DNS is propagating correctly
- Wait a bit longer (up to 1 hour)
- Try clicking "Verify DNS configuration" again

### Issue: "Site shows old content"
**Solution**:
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Try incognito/private mode
- Wait for CDN to update (1-2 minutes)

### Issue: "Cannot add A records at name.com"
**Solution**:
- Check if you have existing A records - delete them first
- Make sure you're using @ or blank for the host field
- Contact name.com support if you get specific error messages

### Issue: "www works but root domain doesn't"
**Solution**:
- Verify all 4 A records are added correctly
- Check that Host field is @ or blank (not "voters-speak.com")
- Wait for DNS propagation

## Alternative: CNAME Flattening (If Supported)

If name.com supports CNAME flattening (also called ALIAS records):

1. Instead of A records, create:
   ```
   Type: ALIAS (or ANAME)
   Host: @ (or blank)
   Answer: dreamy-manatee-714bdc.netlify.app
   ```

This is preferred but not all registrars support it.

## Expected Timeline

1. **Add domain in Netlify**: Immediate
2. **Update DNS at name.com**: 5 minutes
3. **DNS propagation**: 5-30 minutes
4. **SSL certificate**: 5-15 minutes after DNS verification
5. **Total time**: 15-60 minutes typically

## Final Checklist

- [ ] Custom domain added in Netlify
- [ ] CNAME record for www created at name.com
- [ ] Four A records for root domain created at name.com
- [ ] Old conflicting DNS records deleted
- [ ] DNS propagation verified (dnschecker.org)
- [ ] Netlify DNS verification passed
- [ ] SSL certificate provisioned
- [ ] Force HTTPS enabled
- [ ] Site accessible at https://www.voters-speak.com
- [ ] Root domain redirects to www

## Support Resources

- **Netlify DNS Documentation**: https://docs.netlify.com/domains-https/custom-domains/
- **name.com Support**: https://www.name.com/support
- **DNS Checker**: https://dnschecker.org
- **SSL Checker**: https://www.sslshopper.com/ssl-checker.html

## Notes

- Keep your Netlify site URL (dreamy-manatee-714bdc.netlify.app) as backup
- DNS changes are reversible - you can always change back
- SSL certificates renew automatically through Netlify
- No cost for SSL certificates (included with Netlify)

---

**Last Updated**: October 20, 2025
**Netlify Site**: dreamy-manatee-714bdc
**Domain**: www.voters-speak.com