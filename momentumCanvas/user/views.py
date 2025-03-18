from django.shortcuts import render, HttpResponse, redirect
from .models import UserData
import requests
from django.contrib import messages
import requests
from .platformData import platformData




def home(request):
    return render(request, 'user/home.html')


def signIn(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if UserData.objects.filter(email=email).exists():
            user=UserData.objects.get(email=email)
            # print("your baby")
            if password==user.password:
                request.session['competitive_data'] = {
                    'name': user.name,
                    'username': user.username,
                    'phone': user.phone,
                    'email': user.email,
                    'leetcode': user.leetcode,
                    'geekforgeeks': user.geekforgeeks,
                    'codechef': user.codechef,
                    'github': user.github,
                    'codeforces': user.codeforces
                }
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials")
                return render(request, "user/signIn.html")
        else:
            messages.error(request, "Email do not exist")
            return render(request, "user/signIn.html")
        
    return render(request, 'user/signIn.html')



def signUp(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            leetcode = request.POST.get('leetcode')
            codechef = request.POST.get('codechef')
            geekforgeeks = request.POST.get('geekforgeeks')
            codeforces = request.POST.get('codeforces')
            github = request.POST.get('github')
            
            # Check if the username already exists
            if UserData.objects.filter(email=email).exists():
                messages.error(request, "user already exist")
                return render(request, "user/signUp.html")
            else:
                newUser = UserData(
                    name=name,
                    username=username,
                    email=email,
                    phone=phone,
                    password=password,
                    leetcode=leetcode,
                    codechef=codechef,
                    geekforgeeks=geekforgeeks,
                    github=github,
                    codeforces=codeforces
                )
                newUser.save()
               # Redirect to dashboard
                return redirect('signIn')  # Ensure URL name 'dashboard' exists

    except Exception as e:
        return redirect('error')

    return render(request, 'user/signUp.html')




def dashboard(request):
    # Retrieve competitive data from session
    user_competitive_data = request.session.get('competitive_data')

    if not user_competitive_data:
        messages.error(request, "signIn/register first")
        return render(request, 'user/home.html')

    # Extract usernames
    leetcode_username = user_competitive_data.get('leetcode')
    codechef_username = user_competitive_data.get('codechef')
    codeforces_username = user_competitive_data.get('codeforces')
    geekforgeeks_username = user_competitive_data.get('geekforgeeks')
    github_username = user_competitive_data.get('github')

    # Construct the API URLs
    leetcodeUrl = f'https://leetcode-stats-api.herokuapp.com/{leetcode_username}'
    codechefUrl = f'https://codechef-api.vercel.app/handle/{codechef_username}'
    codeforcesUrl = f'https://codeforces.com/api/user.info?handles={codeforces_username}'
    geekforgeeksUrl = f'https://geeks-for-geeks-stats-api.vercel.app/?raw=y&userName={geekforgeeks_username}'
    githubUrl = f'https://api.github.com/users/{github_username}'

    # Initialize empty data
    leetcodeData = {}
    codechefData = {}
    codeforcesData = {}
    geekforgeeksData = {}
    githubData = {}

    github_response = requests.get(githubUrl)
    if github_response.status_code == 200:
        githubData = github_response.json()

    # Send GET request to the LeetCode API
    leetcode_response = requests.get(leetcodeUrl)
    if leetcode_response.status_code == 200:
        leetcodeData = leetcode_response.json()  # Get JSON data from response
    

    # Send GET request to the CodeChef API
    codechef_response = requests.get(codechefUrl)
    if codechef_response.status_code == 200:
        codechefData = codechef_response.json()  # Get JSON data from response
    # else:
    #     return redirect('error')
     
    
    codeforces_response = requests.get(codeforcesUrl)
    if codeforces_response.status_code == 200:
        codeforces_json = codeforces_response.json()
        
        # Extract the first item from the 'result' list to get the user data as a dictionary
        if 'result' in codeforces_json and len(codeforces_json['result']) > 0:
            codeforcesData = codeforces_json['result'][0]
        
    geekforgeeks_response = requests.get(geekforgeeksUrl)
    if geekforgeeks_response.status_code == 200:
        geekforgeeksData = geekforgeeks_response.json()
    # else:
    #     return redirect('error')
        
    # print(geekforgeeksData)
    print(githubData)
    
    # Pass both LeetCode and CodeChef data to the template
    return render(request, 'user/dashboard.html', {
        'leetcodeData': leetcodeData,
        'codechefData': codechefData,
        'geekforgeeksData': geekforgeeksData,
        'codeforcesData' : codeforcesData,
        'githubData' : githubData,
        'user': user_competitive_data.get('username'),
    })



def error(request):
    return render(request, "user/error.html")


def platformDetail(request, platformName):
    # platformDetails = {
    #     "leetcode" : {"title":"Leetcode", "description":"Leetcode is coding platform"},
    #     "codechef" : {"title":"CodeChef", "description":"CodeChef is coding platform"},
    #     "gfg" : {"title":"GeekForGeeks", "description":"GeekForGeeks is coding platform"},
    #     "codeforces" : {"title":"CodeForces", "description":"CodeForces is coding platform"},
    #     "github" : {"title":"Github", "description":"Github is coding platform"},
    # }
  

    platformInfo = platformData.platformDetails.get(platformName, {"title":"Unknown", 
                                                                   "description":"platform not found",
                                                                   "sections":"Nothing to show",
                                                                   })
    return render(request, 'user/platformDetail.html', {"platform":platformInfo})

def analytics(request):
    return render(request, 'user/analytics.html')