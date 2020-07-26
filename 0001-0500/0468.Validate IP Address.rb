# @param {String} ip
# @return {String}
def valid_ip_address(ip)
    if ip.count(".") == 3
        return "IPv4" if ip.split(".") .select { |x| x.to_i.to_s == x && x.to_i >= 0 && x.to_i < 256 } .size == 4
    elsif ip.count(":") == 7
        return "IPv6" if ip.split(":").select { |x| x.size > 0 && x.size <= 4 && x.to_i(16).to_s(16) == x.sub(/^0*/, "").sub(/^$/, "0").downcase }.size == 8
    end
    return "Neither"
end
