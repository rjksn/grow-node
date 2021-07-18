DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Preparing to update grow code"

cd "$DIR/.." && git pull && cd -

echo "Updated grow code"
