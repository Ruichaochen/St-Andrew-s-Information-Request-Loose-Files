_G.collect = true
while _G.collect do
local tbl_main = 
{
      "ClaimPotion", 
      2
}
game:GetService("ReplicatedStorage").NetworkRemoteEvent:FireServer(unpack(tbl_main))
wait(0.1)
local tbl_main = 
{
      "ClaimPotion", 
      1
}
game:GetService("ReplicatedStorage").NetworkRemoteEvent:FireServer(unpack(tbl_main))
wait(0.1)
end