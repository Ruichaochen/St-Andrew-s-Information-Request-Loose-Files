stands = {}
for i,stand in pairs(game:GetService("ReplicatedStorage").StandModel:GetChildren()) do
    if stand.Name ~= "PackageLink" then
        table.insert(stands, stand.Name)
    end
end
clickedbefore = false
local vu = game:GetService("VirtualUser")
game:GetService("Players").LocalPlayer.Idled:connect(
function()
    vu:Button2Down(Vector2.new(0, 0), workspace.CurrentCamera.CFrame)
    wait(math.random(0.3, 1.1))
    vu:Button2Up(Vector2.new(0, 0), workspace.CurrentCamera.CFrame)
end)
local library = loadstring(game:HttpGet("https://raw.githubusercontent.com/GreenDeno/Venyx-UI-Library/main/source.lua"))()
local venyx = library.new("Shrek Hub", 5013109572)

-- themes
local themes = {
	Background = Color3.fromRGB(24, 24, 24), 
	Glow = Color3.fromRGB(0, 0, 0), 
	Accent = Color3.fromRGB(10, 10, 10), 
	LightContrast = Color3.fromRGB(20, 20, 20), 
	DarkContrast = Color3.fromRGB(14, 14, 14),  
	TextColor = Color3.fromRGB(255, 255, 255)
}
-- first page
local Arrows = venyx:addPage("Arrow Stuff", 5012544693)
local section1 = Arrows:addSection("Arrow Stuff")
-- get arrows
section1:addButton("Get Arrows", function()
    if clickedbefore == false then 
    venyx:Notify("", "They added a proximity check so this is less efficient. You may have to press multiple times to get more arrows")
    end
clickedbefore = true
for i,arrow in pairs(game:GetService("Workspace"):GetDescendants()) do
		if arrow.Name == "Stand Arrow" and arrow.Parent == game.Workspace then
		    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = arrow.Handle.CFrame
		    wait(0.3)
			fireclickdetector(arrow.ClickDetector, 4)
		end
end
end)

-- use arrow
section1:addButton("Use Arrow", function()
game:GetService("ReplicatedStorage").ItemEvent.StandArrow:FireServer()
end)

-- second page
local NPCS = venyx:addPage("NPC Stuff", 5012544693)
local section2 = NPCS:addSection("NPCS")

section2:addButton("Reset Stand", function()
   workspace.Pucci.Pucci:FireServer()
   end)

section2:addButton("Get Alain's Quest", function()
	local args = {
		[1] = "Accepted"
	}

	workspace.Alain.Alain:FireServer(unpack(args))
end)
section2:addButton("Get Zai's Quest", function()
	local args = {
		[1] = "Accepted"
	}

	workspace.Zai.Zai:FireServer(unpack(args))
end)

section2:addButton("Get Josuke's Quest", function()
local args = {
    [1] = "Accepted"
}
workspace.Josuke.Josuke:FireServer(unpack(args))
end)
-- Stand farm
local StandFarm = venyx:addPage("Stand Farm", 5012544693)
local Stand = StandFarm:addSection("Stand Farm")

Stand:addDropdown("Dropdown", stands, function(standgetvalue)
    print(standgetvalue .. " selected")
    getgenv().standwanted = standgetvalue
end)
 getgenv().looptoggle = false
Stand:addToggle("Toggle Stand Farm", nil, function(standtoggle)
getgenv().looptoggle = standtoggle
    print(getgenv().looptoggle)
while getgenv().looptoggle do
    if game.Players.LocalPlayer.Character:WaitForChild("StandName").Value ~= getgenv().standwanted then
repeat task.wait()
workspace.Pucci.Pucci:FireServer()
        game:GetService("ReplicatedStorage").ItemEvent.StandArrow:FireServer()
        print(game.Players.LocalPlayer.Character:WaitForChild("StandName").Value)
        wait(4)
until game.Players.LocalPlayer.Character:WaitForChild("StandName").Value == getgenv().standwanted or getgenv().looptoggle == false
wait()
break;
end
end
end)

--discord Stuff
local misc = venyx:addPage("Discord and misc", 5012544693)
local discordsection = misc:addSection("Discord")
local hidegui = misc:addSection("Settings")
local credits = misc:addSection("Credits")
--discord
discordsection:addButton("Copy discord link", function()
   setclipboard("https://discord.gg/cxe5HYB9nZ")
end)
--hide
hidegui:addKeybind("Toggle Keybind", Enum.KeyCode.RightShift, function()
venyx:toggle()
end, function()
end)
--credits
credits:addButton("Developed by Ruichao#8510, Ideas from Shrek", function()
end)
-- load
venyx:SelectPage(venyx.pages[1], true)