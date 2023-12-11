#pragma once

#include <vector>
#include <string>
#include <array>

using Args = std::vector<std::string>;


/// @brief Used to handle argument options, and input, as well as possibly give hints to mistakes
class ArgsHandler {
public:
	ArgsHandler(const int argc, const char* argv[]);
	const Args& GetArgs() const;
private:
	Args args;
};

// For each argument, we could have one, two or all of these three attributes
// One, the argument's value itself
// Two, the argument's little argument (argception lol)
// Three, the argument's functionality 