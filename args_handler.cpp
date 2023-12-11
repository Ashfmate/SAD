#include "args_handler.hpp"

using std::vector, std::string;

ArgsHandler::ArgsHandler(const int argc, const char *argv[]) {
	for (size_t i = 1; i < (size_t)argc; ++i) {
		args.push_back(string(argv[i]));
	}
}

const Args& ArgsHandler::GetArgs() const
{
	return args;
}
